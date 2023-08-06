#include "CNecklace.h"

namespace whycon {

CNecklace::CNecklace(int id_bits, int id_samples, int minimalHamming, bool debug): debug(debug), id_samples(id_samples)
{
    length = id_bits;
    maxID = 0;
    idLength = pow(2, length);
    idArray = (SNecklace*)malloc(sizeof(SNecklace) * idLength);

    int currentID = 0;
    int tempID, bit, rotations;
    int minHam = 1000;
    int hamindex = 1000;
    int ham = 1000;

    /*for every possible id*/
    for (int id = 0; id < idLength; id++)
    {
        /*check if there is a lower number that could be created by id_bitshifting it*/
        tempID  = id;
        rotations = 0;
        int cached [length - 1];
        bool isSymmetrical = false;
        minHam = 1000;
        if (debug) printf("Testing %i\n", tempID);
        do{
            hamindex = getMinimalHamming(tempID, id);
            ham = getHamming(tempID, hamindex);
            if (minHam > ham)
            {
                minHam = ham;
                if (minHam == 0)
                {
                    idArray[id].id = idArray[hamindex].id; 
                    idArray[id].rotation = idArray[hamindex].rotation + rotations; 
                    if (debug) printf("AAA %i %i %i \n", id, idArray[id].id, idArray[id].rotation);
                }
            }
            bit = tempID % 2;
            tempID=tempID / 2 + bit * pow(2, length - 1);

            if(bit || id == 0)
            {
                for (int i = 0; i < rotations && !isSymmetrical; i++)
                {
                    // check for symmetry
                    if (cached[i] == tempID)
                    {
                        isSymmetrical = true;
                    }
                }
            }
            cached[rotations] = tempID; 
            //ham = getMinimalHamming(tempID,id);
            //if (minHam > ham) minHam = ham;
        }while (rotations++ < length - 1 && !isSymmetrical);

        if (minHam >= minimalHamming && !isSymmetrical)
        {
            if (debug) printf("Adding %i %i\n", currentID, id);
            idArray[id].id = currentID++;
            idArray[id].rotation = 0;
            idArray[id].hamming = minHam;
        }
        else if (minHam > 0)
        {
            idArray[id].id = -1; 
            idArray[id].rotation = -1;
            idArray[id].hamming = minHam;
        }
        if(isSymmetrical)
        {
            idArray[id].id = -1;
            idArray[id].rotation = -1;
        } 
    }

    //idArray[idLength-1].id = 0;
    //idArray[idLength-1].rotation = 0;
    unknown.id = -1;
    unknown.rotation = -1;

    for (int i = 0; i < idLength; i++)
    {
        if(maxID < idArray[i].id) maxID = idArray[i].id;
        
    }


    probArray = (float*)malloc(sizeof(float) * maxID);
    for (int id = 0; id < maxID; id++) {
        probArray[id] = 1. / (float)maxID;
    }
}

CNecklace::~CNecklace()
{
    free(idArray);
    free(probArray);
}

int CNecklace::getHamming(int a, int b)
{
    int aa = a;
    int bb = b;
    int ham = 0;
    do {
        if (a % 2 != b % 2) ham++;
        a = a / 2;
        b = b / 2;
    }while (a > 0 || b > 0);
    if (debug) printf("Hamming %i %i is %i\n", aa, bb, ham);
    return ham;
}

int CNecklace::getMinimalHamming(int a, int len)
{
    int minDist = 10000;
    int mindex = 10000;
    for (int i = 1; i < len; i++)
    {
        if (get(i, false).rotation == 0)
        {
            int m = getHamming(a, i);
            if (minDist > m)
            {
                minDist = m;
                mindex = i;
                //if (minDist < 3) printf("%i is same as %i\n",a,i);
            }
        }
    }
    if (debug) printf("Minimal hamming of %i is %i\n", a, minDist);
    return mindex;
    //return minDist;
}

int CNecklace::verifyHamming(int a[], int id_bits, int len)
{
    int overAll = 10000;
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            int minimal = 10000;
            if (i != j)
            {
                int bit;
                int tempID = a[j];
                int distance;
                if (debug) printf("Testing %i vs %i\n", a[i], a[j]);
                for (int r = 0; r < id_bits; r++)
                {
                    distance = getHamming(a[i], tempID);
                    if (debug) printf("Test %i %i %i\n", a[i], tempID, distance);
                    if (minimal > distance) minimal = distance;
                    bit = tempID % 2;
                    tempID=tempID / 2 + bit * pow(2, length - 1);
                }
            }
            if (debug) printf("%i vs %i has %i\n",a[i],a[j],minimal);
            if (overAll > minimal) overAll = minimal;
        }
    }
    return overAll;
}

SNecklace CNecklace::get(int sequence, bool probabilistic, float confidence)
{
    // default parameters: bool probabilistic = false, float confidence = 1.0
    // idLength = pow(2, length); it is 16 for length=4 bits

    if (sequence <= 0 || sequence >= idLength) return unknown;
    if (!probabilistic) return idArray[sequence];

    float oe = observationEstimation(confidence);  // 0.121 for MaxId=16, confidence=1
    float o = .0;

    for (int i = 0; i < maxID; i++)
    {
        if (idArray[sequence].id == i) o += (oe * probArray[i]);
        else o += ((1.0 - oe) / (float)(maxID - 1) * probArray[i]);
    }

    for (int i = 0; i < maxID; i++)
    {
        if (idArray[sequence].id == i ) probArray[i] = (oe / o) * probArray[i];
        else probArray[i] = (1.0 - oe) / (float)(maxID - 1) / o * probArray[i];

        if(probArray[i] <= 1. / maxID)
        {
            if (debug) printf("Confidence value too small, changing %.9f to %.9f\n", probArray[i], 1. / maxID);
            probArray[i] = 1. / maxID;
        }

        if(probArray[i] > 1. - (1. / maxID))
        {
            if(debug) printf("Confidence value too big, changing %.9f to %.9f\n", probArray[i], 1. - (1. / maxID));
            probArray[i] = 1. - (1. / maxID);
        }
    }
    SNecklace toReturn = idArray[sequence];
    toReturn.id = getEstimatedID();
    return toReturn;
}

float CNecklace::observationEstimation(float confidence)
{
    float a = 400.;
    float s = 80.;
    return atan2((confidence - a), s) * ((1. - (1. / (float)maxID)) / M_PI) + (((float)maxID + 1.) / (2. * (float)maxID));
}

int CNecklace::getEstimatedID()
{
    int hp = 0;
    for (int id = 0; id < maxID; id++)
    {
        if (debug) printf("%i %f\n", id, probArray[id]);
        if(probArray[id] > probArray[hp]) hp = id;
    }
    // printf("%i\n", hp+1);
    return hp;
}

SDecoded CNecklace::decode(char *code, char *realCode, int max_index, float segmentV0, float segmentV1)
{
    // "length" is the number of bits.
    // "realCode" is buffer for string, (char realCode[id_bits + 1]; id_bits==length)
    
    // if (debug) printf("CNecklace::decode code:%s, max_index:%i, segmentV0:%f, segmentV1:%f, length:%i,\n", code, max_index, segmentV0, segmentV1, length);
    // determine the control edges' positions
    int edge_index = 0;
    // Iteration over pair of bits.  Searches for a last sequence of two consecutive zeros.
    for (int a = 0; a < length * 2; a++)
    {
        int p = (a + 1) % (length * 2);
        if (code[a] == '0' && code[p] == '0') edge_index = a;
    }
    edge_index = 1 - (edge_index % 2); // 0 or 1

    // Iteration over bits.  Construct ID.
    int ID = 0;
    for (int a = 0; a < length; a++)
    {
        realCode[a] = code[edge_index + 2 * a]; // Insert every other character from the edge_index

        //if (realCode[a] == 'X') ID = -1; /*TODO note #01*/
        //if (ID > -1){ /*TODO note #02*/

            ID = ID * 2;                    // shif ID to left
            if (realCode[a] == '1') ID++;   // add leftmost 1 (if in the result)
        //}
    }
    realCode[length] = 0;   // add terminal char
    // if (debug) printf("Ivo: ID:%i, realCode:%s\n", ID, realCode);
    SNecklace result = get(ID);
    // if (debug) printf("Ivo: SNecklace result = get(%i): id:%i, rotation:%i, hamming:%i\n", ID, result.id, result.rotation, result.hamming);

    //float segmentAngle;
    //segmentAngle = 2*M_PI*(-(float)max_index/id_samples+(float)result.rotation/length)+atan2(segmentV1,segmentV0)+1.5*M_PI/length;
    float segmentAngle = 2*M_PI*(-(float)max_index/id_samples-(float)edge_index/length/2.0+(float)result.rotation/length)+atan2(segmentV1,segmentV0);//+1.5*M_PI/length;
    
    while (segmentAngle > +M_PI) segmentAngle -= 2 * M_PI;
    while (segmentAngle < -M_PI) segmentAngle += 2 * M_PI;

    SDecoded out;
    out.angle = segmentAngle;
    out.id = result.id++;
    // if (debug) printf("Ivo: marker decoded ID:%i, edge_index:%d, axis rotation angle:%f\n", out.id, out.edge_index, out.angle);
    out.edge_index = edge_index;
    return out;
}

} // namespace whycon
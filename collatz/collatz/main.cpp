//
//  main.cpp
//  collatz
//
//  Created by Phil Nova on 7/12/15.
//  Copyright (c) 2015 Phil Nova. All rights reserved.
//

#include <iostream>
#include <ctime>
using namespace std;

int collatz_naive(unsigned long val) {
    int counter = 0;
    
    while (val != 1) {
        if (val % 2 == 0)
            val = val / 2;
        else
            val = (3 * val) + 1;
        counter ++;
        //cout << val << endl;
    }
    
    return counter;
}

pair<int,int> max_collatz_naive(int limit) {
    int max_chain = 0;
    int max_collatz = 0;
    int current_chain = 0;
    for (int i=1; i<limit; i++){
        //cout << i << endl;
        current_chain = collatz_naive(i);
        if (current_chain > max_chain) {
            max_chain = current_chain;
            max_collatz = i;
        }
    }
    //cout << max_chain << " " << max_collatz << endl;
    return make_pair(max_chain, max_collatz);
}

int collatz_array[1];

int collatz_cached(unsigned long val, int limit) {
    int counter = 0;
    int original_val = val;
    
    while (val > limit - 1 or collatz_array[val] == 0){
        if (val % 2 == 0)
            val = val / 2;
        else
            val = (3 * val) + 1;
        counter ++;
        //need to add result to a dynamic array
    }
    
    return 0;
}

pair<int,int> max_collatz_cached(int limit) {
    int max_chain = 0;
    int max_collatz = 0;
    int current_chain = 0;
    
    int collatz_array[limit];
    collatz_array[1] = 1;
    
    for (int i=1; i<limit; i++){
        current_chain = collatz_cached(i,limit);
        if (current_chain > max_chain) {
            max_chain = current_chain;
            max_collatz = i;
        }
    }

    
    
    return make_pair(max_chain, max_collatz);
}


int main(int argc, const char * argv[]) {
    //int output = collatz_naive(113383);
    //cout << output;
    double starttime;
    //starttime = clock();
    pair<int,int>answer = max_collatz_naive(1000000);
    cout << "Max chain length = " << answer.first << " at integer = " << answer.second << endl << " in " << (clock() - starttime)/CLOCKS_PER_SEC << endl;
    return 0;
}

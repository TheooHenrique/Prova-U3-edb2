#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n, m;

    cin >> n;
    vector<int> vec;
    vector<int> resposta;

    for(int i{0}; i < n; ++i){
        cin >> m;
        vec.push_back(m);
    }

    for (int i{0}; i < vec.size(); ++i){

        int key = vec[i];
        vector<int> vecCopy = vec;

        vecCopy.erase(vecCopy.begin() + i);
        auto a = find(vecCopy.begin(), vecCopy.end(), key);
        if (a == vecCopy.end()){
            resposta.push_back(i + 1);
        }
    }

    if (resposta.empty()) cout << -1;
    else{
        cout << endl << *max_element(resposta.begin(), resposta.end()) << endl;
    }
    
    return 0;
}
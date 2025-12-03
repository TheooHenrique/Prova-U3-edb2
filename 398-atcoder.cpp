#include <iostream>
#include <map>
#include <ostream>
#include <set>
#include <utility>

int main(){
    int n, m;
    std::cin >> n;

    std::map<int, int> map;
    std::map<int, int> map2;
    std::set<int> set;
    std::set<int> set2;


    for(int i{0}; i < n; ++i){
        std::cin >> m;

        if (map.find(m) == map.end()){
            map.insert(std::pair<int, int>(m, i + 1));
            map2.insert(std::pair<int, int>(m, i + 1));
        } else{
            map2.erase(m);
        }
    }

    auto maior = map2.rbegin();

    if (map2.empty()) std::cout << -1;
    else std::cout << maior->second;
    return 0;
}
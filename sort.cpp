#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <vector>

#define print(x) std::cout << x << '\n'


std::string eval(std::string s){
 std::string ans(26,'0');
 for(char i:s){
  int x = i;
  char &b = ans[x - 97];
  int y = b;
  b = y + 1;
 }
 return ans;
}

std::map <std::string,std::vector<std::string>> d;
int main(){

 std::ifstream f;
 f.open("english.txt" , std::ios::in);
 std::string line;
 while (f){
  std::getline(f,line);
  if (line.size() < 4){
   continue;
  }
  d[eval(line)].push_back(line);
 }
 f.close();	
 print("Completed reading file");
 std::ofstream f1;
 f1.open("anagrams.txt",std::ios::out);
 for(auto i:d){
  if(i.second.size() == 1){
   continue;
  }
  for(auto j:i.second){
   f1 << j << ' ';
  }
  f1 << '\n';
 }
 f1.close();
}

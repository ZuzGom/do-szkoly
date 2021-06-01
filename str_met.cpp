 1 #include <iostream> 
 2 #include <cstring> 
 3  
 4 using namespace std; 
 5  
 6 int main() 
 7 { 
 8 string lancuch="Zespol Szkol nr 4 w Jasle"; 
 9 string lan1="Ala", lan2="Ola"; 
10 char kopia[100]; 
11 int dl=lancuch.size(); 
12 //Metoda max_size() zwraca maksymaln¹ wielkoœæ stringa, na jak¹ dane œrodowisko mo¿e pozwoliæ. Nale¿y wzi¹æ pod uwagê inne ograniczenia, takie jak pamiêæ operacyjna, które mog¹ nie pozwoliæ nam przydzieliæ tak wielkiego obiektu string. 
13 lancuch.max_size(); 
14 //Metoda insert() dodaje pod³añcuch do danego ³¹ñcucha od danej pozycji 
15 lancuch.insert(0,"Szkola "); 
16 cout<<lancuch<<endl; 
17 //Metoda append() dodaje pod³añcuch na koniec danego ³añcucha 
18 lancuch.append("- to najlepsza szkola"); 
19 cout<<lancuch<<endl; 
20 //Metoda push_back() dodaje znak na koniec danego lancucha 
21 lancuch.push_back('!'); 
22 cout<<lancuch<<endl; 
23 //Metoda pop_back() usuwa ostatni znak z lancucha 
24 lancuch.pop_back(); 
25 cout<<lancuch<<endl; 
26 cout<<lancuch.substr(1, 4)<<endl; 
27 // Metoda clear() usuwa znaki z lancucha(Mo?na uzy? lancuch="";); 
28 //lancuch.clear(); 
29 //Metoda empty() sprawdza czy lancuch jest pusty 
30 cout<<lancuch.empty()<<endl; 
31 //Metoda find() zwraca pozycj? pierwszego wyst?pienia frazy podanej jako argument lub zwraca wartoœæ string::npoz w sytuacji, gdy fraza nie zostanie odszukana. 
32 cout<<lancuch.find("Jasle")<<endl; 
33 lan1.swap(lan2); 
34 cout<<lan1<<" "<<lan2; 
35 //Metoda copy() kopiuje fragment ?a?cucha do tablicy znaków 
36 cout<<lancuch.copy(kopia,2,4); 
37 //Metoda c_str() zamienia ?a?cuch na tablic? znaków 
38 lancuch.c_str() 
39 strcpy(tab,lancuch.c_str()); 
40 return 0; 

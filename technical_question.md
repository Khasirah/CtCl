# Technical Question
## How To Prepare
lakukan hal-hal berikut:
1. try to solve the problem on your own
2. write the code on paper
3. test your code - on paper
4. type your code as-is into a computer. kamu mungkin akan menemukan kesalahan, catat kesalahan tersebut jadi kamu bisa menyimpannya di memeori selama interview berlangsung
5. do as many mock interview 

## what you need to know
### core data structure, algorithms, and concept
- know the basic of data structure
- know the basic of algorithm
- must have knowledge

| data structure | algorithm | concept |
| ---- | ---- | ---- | 
| linked list | breadth-first search | bit manipulation |
| tree, tries & graph | depth-first search | memory (stack vs heap) |
| stack & queues | binary search | recursion |
| heap | merge sort | dynamic programming |
| vector / arrayList | quick sort | big o time & space |
| hash table | |

**noted:** make sure understand how to use and implementing them, and where applicable, the space and time complexity

### powers of 2 table 
- berguna untuk pertanyaan tentang "***scalability***" atau "***sort of memory limitaion***" 

| power of 2 | exact value (x) | appox. value | x bytes int MB, GB, etc |
| ---- | ---- | ---- | ---- |
| 7 | 128 | | |
| 8 | 256 | | |
| 10 | 1024 | 1 thousand | 1 KB |
| 16 | 65.536 | | 64 KB |
| 20 | 1.048.576 | 1 million | 1 MB |
| 30 | 1.073.741.824 | 1 billion | 1 GB |
| 32 | 4.294.967.296 | | 4 GB |
| 40 | 1.099.511.627.776 | 1 trillion | 1 TB |

## walking through a problem
### Problem Solving Flowchart
```mermaid
flowchart TB 
subgraph S1[" "]
direction LR 
  N1(listen <br/> <b>pay very close attention</b><br/>to any information in the problem description.<br/>you probably need it all for an optimal algorithm.)
  N2(example<br/> <b>debug your example</b><br/>is there any way its a special case? is it big enough?)
  
  N1 --> N2
end

subgraph S2[" "]
direction RL
  N3(Brute Force<br/>get a brute force solution as soon as possbile.<br/>dont worry about developing an efficient algorithm yet.<br/>state a naive algorithm and its runtime,<br/> than optimize from there.<br/> dont code yet though!)
  N4(BUD Optimize<br/>Bottleneck<br/>Unnecessary work<br/>duplicated work)

  N3 --> N4
end

subgraph S3[" "]
direction LR
  N5("Test
  test in this order:
  1. tes konsep. telusuri code mu seperti 
  kamu akan di review secara detail
  2. unusual or no-standard code 
  3. hot spots, like arithmatic and null nodes
  4. small test case, 
  its much faster than a big test case
  5. special case adn edge case
  and when you find bugs, fix them carefully")
  N6("Optimize 
  walk through your brute force with BUD
  optimization or try some of these ideas:
  - look for unused info. you usually
  need all the information in a problem 
  - solve it manually on an example, then
  reverse engineer your through process.
  how do you solve it?
  - make a time vs space tradeoff. 
  hash tables are especially usefull")

  N5 --> N6
end

subgraph S4[" "]
direction RL
  N7("walk through
  now that you have an optimal solution, 
  walk through your approach in detail. make sure 
  you understand each detail before you start 
  coding")
  N8("implement 
  your goal is to write beautiful code 
  modularize your code from the 
  beginning and refactor to clean up
  anything that isn't beautiful")

  N7 --> N8
end

S1 --> S2
S2 --> S3
S3 --> S4
```
**Keep talking!** your interviewer wants to hear how you approach the problem

<<<<<<< HEAD
---

=======
## Optimize & solve technique #1: Look for BUD 
- Bottleneck 
- Unnecessary work 
- Duplicated work

#### Bottleneck 
bottleneck adalah bagian dari algorima mu yang membuat lambat keseluruhan runtime. terdapat 2 kebiasaan yang dapat menyebabkannya muncul:
1. terdapat satu pekerjaan yang membuat lambat algorima mu 
> contoh: semisal km memiliki 2 step algoritma dimana yang pertama adalah  "*sort array*" dan kemudian menemukan elemen dengan properti tertentu
>
> langkah pertama: is O(N log N) <br/>
> langkah kedua: O(N) <br/>
> mungkn kamu bisa mengurangi langkah kedua dengan O(log N) atau O(1) tapi apakah itu berguna? tidak begitu banyak<br/>
> bottleneck nya adalah langkah pertama O(N log N) <br/>
> jadi kita harus melakukan optimalisasi pada langkat pertama, sampai itu terjadi *overall runtime* menjadi O(N log N)
2. terdapat banyak pekerjaan atau fungsi (pada program seperti *for loop*), mungkin bisa dikurangi dari O(N) menjadi O(log N) atau bahkan O(1)

> ### contoh kasus optimilisasi bottleneck
> given an array of distinct integer values, count the number of pairs of integers that have difference k. for example, given the array {1, 7, 5, 9, 2, 12, ,3} and the difference k =2, there are four pairs with difference 2: (1, 3), (3,5), (5,7), (7,9)

- brute force (pemikiran kasar) go through the array, starting form the first element
- search through the remaining elements (which will form the other side of the pair). for each pair, compute the difference. if the difference equls k, increment a counter of the difference

> disini terdapat bottleneck pada saat perulangan pencarian untuk "other side of the pair". yang perlu dilakukan optimalisasi
>
> bagaimana cara menemukan bagian kanannya? (x, ?) <br />
> kita tau bahwa sisi bagian kanannya adalah x + n atau x - n ya kan <br/>
> jika kita mengurutkan array nya maka kita bisa menmunkan bagian kanan untuk setiap elemen dengan runtime O(log N) dengan menggunakan "*binary search*"
>
> sekarang kita memiliki 2 langkah, dimana keduanya O(N log N) time. mengurutkan adalah bottleneck baru. bagaimana cara menemukan pasangan tanpa mengurutkan arraynya. <br/>
> **dengan menggunakan "*hash table*" --> how can we find things quickly in an unsorted array?**
>
> pindahkan semua yang ada di dalam array ke hash table. kemudian, cari  `if x + k or x - k` exist di dalam array kita hanya perlu mencari pada hash table.
>
> dengan ini kecepatan algorima menjadi O(N)
#### Unnecessary work 
> contoh: print all positive integer solutions to the equation `a^3 + b^3 = c^3 + d^3` where a,b,c,d are integer between 1 and 1000

solusi kasarnya adalah 4 "*for loop*", seperti berikut:
```
n = 1000 
for a from 1 to n 
  for b from 1 to n 
    for c from 1 to n 
      for d from 1 to n 
        if a^3 + b^3 = c^3 + d^3 
          print a,b,c,d 
```
terdpat Unnecessary work dalam pengecekan untuk kemungkinan d yang lain, hanya ada satu yang akan bekerja. **setidaknya kita harus "*break*" setelah kita menemukan valid solution**
```
n = 1000 
for a from 1 to n 
  for b from 1 to n 
    for c from 1 to n 
      for d from 1 to n 
        if a^3 + b^3 = c^3 + d^3 
          print a,b,c,d 
          break // break out of d's loop
```
tidak akan banyak berdampak karena runtime tetap O(N<sup>4</sup>) tapi tetap bagus

apakah terdapat Unnecessary work yang lain? yes, jika hanya terdapat satu nilai d yang valid untuk (a,b,c) maka kita bisa menjadikannya `d = (a^3 + b^3 - c^3)^1/3`
```
n = 1000 
for a from 1 to n 
  for b from 1 to n 
    for c from 1 to n 
      d = pow(a^3 + b^3 - c^3, 1/3) // will round to int 
      if a^3 + b^3 = c^3 + d^3
        print a,b,c,d
```
this will reduce our runtime from O(N<sup>4</sup>) to O(N<sup>3</sup>)
>>>>>>> origin/main


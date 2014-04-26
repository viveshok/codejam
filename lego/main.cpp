// solution for https://www.hackerrank.com/challenges/lego-blocks
#include <iostream>
#include <fstream>
#include <map>
#include <deque>
#include <vector>
#include <set>
#include <cstring>
#include <algorithm>
 
using namespace std;
#define coutfpre(n,f) (setiosflags(ios::fixed)<<setprecision(n)<<f)
#define zero(n) memset(n,0,sizeof(n))
#define m1set(n) memset(n,-1,sizeof(n))
#define min(m,n) ((m<n)?m:n)
#define max(m,n) ((m>n)?m:n)
 
#define FILE_TEST
 
#define mo(m) if(m > 1000000007) m = m%1000000007
 
bool solve(istream &in,ostream &out)
{
    int t,hMax = 0,wMax = 0;
 
    in >> t;
    vector <int> vH(t);
    vector <int> vW(t);
 
    for(int i = 0; i < t;i++)
    {
        in >> vH[i] >> vW[i];
        if(vH[i] > hMax)
            hMax = vH[i];
 
        if(vW[i] > wMax)
            wMax = vW[i];
    }
    if(hMax < 4)
        hMax = 4;
    if(wMax < 4)
        wMax = 4;
 
    vector <int> rNumb(wMax + 1,0);
    vector <vector <int> > rNumbPwh(hMax + 1,rNumb);
    vector <vector <int> > rt(hMax + 1,rNumb);
    vector <int> hNumb(hMax + 1,0);
 
    for(int i = 0; i < t;i++)
    {
        if(vW[i] > hNumb[vH[i]])
             hNumb[vH[i]] = vW[i];
    }
 
    rNumb[0] = 1;
    rNumb[1] = 1;
    rNumb[2] = 2;
    rNumb[3] = 4;
    rNumb[4] = 8;
 
    for(int i = 5; i <= wMax; i++)
    {
        rNumb[i] += rNumb[i-4];
        mo(rNumb[i]);
        rNumb[i] += rNumb[i-3];
        mo(rNumb[i]);
        rNumb[i] += rNumb[i-2];
        mo(rNumb[i]);
        rNumb[i] += rNumb[i-1];
        mo(rNumb[i]);
    }
 
    for(int i = 1; i <= wMax; i++)
    {
        long long rNumbTimes = rNumb[i];
        for(int j = 1;j <= hMax ;j++)
        {
            rNumbPwh[j][i] =  rNumbTimes;
            rNumbTimes *= rNumb[i];
            mo(rNumbTimes);
        }
    }
 
    rt[1][1] = 1;
    rt[1][2] = 1;
    rt[1][3] = 1;
    rt[1][4] = 1;
 
    for(int i = 2 ; i <= hMax ; i++)
        rt[i][1] = 1;
 
 
    for(int j = 2;j <= hMax ;j++)
    {
        for(int i = 2; i <= hNumb[j]; i++)
        {
            long long rTemp = rNumbPwh[j][i];
            for(int k = 1 ;k < i ; k++)
            {
                long long rTemp2 = ((long long) rt[j][k] )* ((long long) rNumbPwh[j][i-k]);
                mo(rTemp2);
 
                if(rTemp2 > rTemp)
                {
                    rTemp = rTemp + 1000000007 - rTemp2;
                }
                else
                    rTemp -= rTemp2;
            }
            rt[j][i] = rTemp;
        }
    }
 
    for(int i = 0; i < t;i++)
    {
        out << "N: " << vH[i] << ", M: " << vW[i] << ", result: " << rt[vH[i]][vW[i]]<<endl;
    }
 
    return true;
}
 
 
 
int main()
{
    bool bSolved;
#ifdef FILE_TEST
    ifstream in("input.txt");
    ofstream out("temp.txt");
    if(!in)
    {
        cout<<"file in error\n";
        return 0;
    }
    if(!out)
    {
        cout<<"file out error\n";
        in.close();
        return 0;
    }
    bSolved = solve(in,out);
    in.close();
    out.close();
#else
    bSolved = solve(cin,cout);
#endif
 
#ifdef FILE_TEST
    if(!bSolved)
        cout << "not solved\n" <<endl;
    else
        cout << "solved\n" <<endl;
    //getchar();
#endif
 
    return 0;
}


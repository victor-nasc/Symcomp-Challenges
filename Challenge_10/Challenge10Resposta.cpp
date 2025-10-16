#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

int sum(vector<int> &e, int N) {
    int soma = 0;
    for(int i = 0; i < N; i++) {
        soma += e[i];
    }
    return soma;
}

int max_value(vector<int> &e, int N) {
    int m = 0;
    for(int i = 0; i < N; i++) {
        m = max(m, e[i]);
    }
    return m;
}

void busca_binaria(vector<int> &e, int N, int K) {
    int i = max_value(e, N), j = sum(e, N);

    while(i <= j) {
        int mid = i + (j - i)/2;
        
    }
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    cin >> N >> K;

    vector<int> e(N);
    for(int i = 0; i < N; i++) {
        cin >> e[i];
    }   
}
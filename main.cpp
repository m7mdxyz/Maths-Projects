//  Transportation problem (North‑West Corner method)
//  Author:  Mohammed .
//  Course:  MATH 329 – Operations Research
//  Year:    2022
//  License: MIT

#include <iostream>
#include <iomanip>

struct coordinates
{
    int x, y;
};

void northWestCorner(double *a, double *b, double **c, int m, int n, double **x)
{
    // copy supply and demand
    double *aa = new double[m];
    double *bb = new double[n];
    for (int i = 0; i < m; ++i) aa[i] = a[i];
    for (int i = 0; i < n; ++i) bb[i] = b[i];

    // initialise decision matrix
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            x[i][j] = 0.0;

    int row = 0, col = 0;
    int iter = 0;
    while ((row < m) && (col < n))
    {
        if (++iter > (m + n)) break;   // safety guard

        if (aa[row] > bb[col]) {
            x[row][col] = bb[col];
            aa[row] -= bb[col];
            bb[col]  = 0.0;
            ++col;
        } else {
            x[row][col] = aa[row];
            bb[col]    -= aa[row];
            aa[row]     = 0.0;
            ++row;
        }
    }

    double sum = 0.0;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            sum += c[i][j] * x[i][j];

    std::cout << "\nTotal shipping cost = " << sum << "\n";
}

int main()
{
    int m, n;
    std::cout << "Enter number of sources: ";
    std::cin >> m;
    std::cout << "Enter number of destinations: ";
    std::cin >> n;

    double *a = new double[m];      // supply
    double *b = new double[n];      // demand
    double **x = new double*[m];    // decision vars
    for (int i = 0; i < m; ++i) {
        x[i] = new double[n];
    }

    std::cout << "\nEnter the supply at the sources:\n";
    for (int i = 0; i < m; ++i) {
        std::cout << "Supply at source " << i+1 << ": ";
        std::cin >> a[i];
    }

    std::cout << "\nEnter the demand at the destinations:\n";
    for (int i = 0; i < n; ++i) {
        std::cout << "Demand at destination " << i+1 << ": ";
        std::cin >> b[i];
    }

    double **c = new double*[m];    // cost matrix
    for (int i = 0; i < m; ++i) {
        c[i] = new double[n];
    }

    std::cout << "\nEnter the costs for the tableau [row][column]:\n";
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
        {
            std::cout << "Enter cost[" << i+1 << "][" << j+1 << "]: ";
            std::cin >> c[i][j];
        }

    northWestCorner(a, b, c, m, n, x);

    // cleanup (not strictly necessary for such a short program)
    for (int i = 0; i < m; ++i) {
        delete[] x[i];
        delete[] c[i];
    }
    delete[] x;
    delete[] a;
    delete[] b;
    delete[] c;

    return 0;
}

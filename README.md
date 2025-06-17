step to do after the cloning<br>
pip install Flask networkx<br>
python app.py<br>
ctrl c to exit the task<br> 

Got it! Here’s the same combined code with numbered headings for each program — ready to copy-paste:

// 1. FactorialRecursive
public class FactorialRecursive {
    public static long factorial(int n) {
        if (n == 0)
            return 1;
        return n * factorial(n - 1);
    }
    public static void main(String[] args) {
        int n = 5;
        System.out.println("Factorial: " + factorial(n));
    }
}

// 2. SequentialSearch
public class SequentialSearch {
    public static int search(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key)
                return i;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] arr = {4, 2, 7, 1, 3};
        int key = 7;
        System.out.println("Found at index: " + search(arr, key));
    }
}

// 3. BinarySearch
public class BinarySearch {
    public static int search(int[] arr, int key, int low, int high) {
        if (low > high) return -1;
        int mid = (low + high) / 2;
        if (arr[mid] == key) return mid;
        else if (arr[mid] < key) return search(arr, key, mid + 1, high);
        else return search(arr, key, low, mid - 1);
    }
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9};
        System.out.println("Found at index: " + search(arr, 5, 0, arr.length - 1));
    }
}

// 4. LCMCalculator
public class LCMCalculator {
    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    private static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
    private static int lcmArray(int[] arr) {
        int result = arr[0];
        for (int i = 1; i < arr.length; i++) result = lcm(result, arr[i]);
        return result;
    }
    public static void main(String[] args) {
        int[] numbers = {12, 15, 20, 25};
        System.out.println("LCM: " + lcmArray(numbers));
    }
}

// 5. EuclidGCD
public class EuclidGCD {
    public static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
    public static void main(String[] args) {
        int a = 56, b = 98;
        System.out.println("GCD: " + gcd(a, b));
    }
}

// 6. SelectionSort
public class SelectionSort {
    public static void main(String[] args) {
        int[] a = {64, 25, 12, 22, 11};
        for (int i = 0; i < a.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = a[i];
            a[i] = a[minIndex];
            a[minIndex] = temp;
        }
        for (int num : a) {
            System.out.print(num + " ");
        }
    }
}

// 7. Dijkstra
import java.util.*;
public class Dijkstra {
    static int min(int[] d, boolean[] v) {
        int m = Integer.MAX_VALUE, i = -1;
        for (int j = 0; j < d.length; j++) if (!v[j] && d[j] < m) { m = d[j]; i = j; }
        return i;
    }
    static void dj(int[][] g, int s) {
        int n = g.length, d[] = new int[n];
        boolean[] v = new boolean[n];
        Arrays.fill(d, Integer.MAX_VALUE);
        d[s] = 0;
        for (int i = 0; i < n; i++) {
            int u = min(d, v); if (u == -1) break; v[u] = true;
            for (int j = 0; j < n; j++)
                if (!v[j] && g[u][j] > 0 && d[u] + g[u][j] < d[j])
                    d[j] = d[u] + g[u][j];
        }
        System.out.println(Arrays.toString(d));
    }
    public static void main(String[] a) {
        int[][] g = {
            {0,1,1,2,0,0,0},
            {1,0,2,0,0,3,0},
            {1,2,0,1,3,0,0},
            {2,0,1,0,2,0,1},
            {0,0,3,2,0,2,0},
            {0,3,0,0,2,0,1},
            {0,2,0,1,0,1,0}
        };
        dj(g, 0);
    }
}

// 8. APSP (Floyd Warshall)
public class APSP {
    static final int I = 99999, V = 4;
    void fw(int[][] d) {
        for (int k = 0; k < V; k++)
            for (int i = 0; i < V; i++)
                for (int j = 0; j < V; j++)
                    if (d[i][k] + d[k][j] < d[i][j])
                        d[i][j] = d[i][k] + d[k][j];
        print(d);
    }
    void print(int[][] d) {
        for (int[] r : d) {
            for (int x : r)
                System.out.print((x == I ? "INF" : x) + " ");
            System.out.println();
        }
    }
    public static void main(String[] a) {
        int[][] g = {
            {0, 5, I, 10},
            {I, 0, 3, I},
            {I, I, 0, 1},
            {I, I, I, 0}
        };
        new APSP().fw(g);
    }
}

// 9. MergeSort
import java.util.Arrays;
public class MSort {
    public static void main(String[] a) {
        int[] arr = {6,3,8,5,2};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
    static void sort(int[] a) {
        if (a.length < 2) return;
        int[] l = Arrays.copyOfRange(a, 0, a.length / 2);
        int[] r = Arrays.copyOfRange(a, a.length / 2, a.length);
        sort(l);
        sort(r);
        merge(a, l, r);
    }
    static void merge(int[] a, int[] l, int[] r) {
        int i = 0, j = 0, k = 0;
        while(i < l.length && j < r.length) {
            if(l[i] < r[j]) a[k++] = l[i++];
            else a[k++] = r[j++];
        }
        while(i < l.length) a[k++] = l[i++];
        while(j < r.length) a[k++] = r[j++];
    }
}

// 10. QuickSort
public class QuickSort {
    public static void main(String[] a) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        sort(arr, 0, arr.length - 1);
        for (int n: arr) System.out.print(n + " ");
    }
    static void sort(int[] a, int l, int h) {
        if (l < h) {
            int p = partition(a, l, h);
            sort(a, l, p - 1);
            sort(a, p + 1, h);
        }
    }
    static int partition(int[] a, int l, int h) {
        int pivot = a[h];
        int i = l - 1;
        for (int j = l; j < h; j++) {
            if (a[j] <= pivot) {
                i++;
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        int temp = a[i + 1];
        a[i + 1] = a[h];
        a[h] = temp;
        return i + 1;
    }
}


---

You can copy all of this at once and paste it into your README or any other file.
If you want me to prepare it in any other format or with extra details, just ask!


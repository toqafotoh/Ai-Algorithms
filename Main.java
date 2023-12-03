import java.awt.*;
import java.util.ArrayList;
import java.util.List;
public class Main {
    static int n = 4;
    static int[] queens = new int[n];
    //queens is an array that contains which position the queen will be placed
    static List<int[][]> solutions = new ArrayList<>();
    //this is an array contains all possible solutions
    static int solutionCount = 0;
    // اسمه واضح بتهيألي
    public static void main(String[] args) {
        queen_test(0,4);
        System.out.println("Number of solutions: " + solutionCount);
        printSolutions();
    }
    public static void queen_test (int trail, int n){
        for(int i=0;i<n;i++){ //try for all columns
            if (test(trail,i)){
                queens[trail]=i;
                if (trail==n-1) { //that means it's the last queen
                    saveSolution();
                    return;
                }
                else {
                    queen_test(trail + 1, n);//test the next queen position
                }
            }
        }
    }

    private static boolean test(int trail, int i) {
        for(int j=0;j<trail;j++){ //check the previous queens
            if ((queens[j] == i) || (Math.abs(queens[j]-i) == Math.abs(j-trail)))
                //that means the column has already a queen
                return false;
        }
        return true;
    }

    private static void saveSolution() {
        int[][] solution = new int[n][n];
        for (int i = 0; i < n; i++) {
            solution[i][queens[i]] = 1;
        }
        solutions.add(solution);
        solutionCount++;
    }

    private static void printSolutions() {
        for (int[][] solution : solutions) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(solution[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
}

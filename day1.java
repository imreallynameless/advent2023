import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner;

public class day1 {
  public static void main(String[] args) {
    File input = new File("day1.txt");
    int sum = 0;
    Array nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    for (string line : input) {
        line = line.trim();
        String toAdd;
        char last;
        Bool first = true;
        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) in nums) {
                if (first) {
                    toAdd += line.charAt(i);
                    last = line.charAt(i);
                    first = false;
                } else {
                    last = line.charAt(i);
                }
            }

        }
    toAdd = toAdd + last;
    sum += Integer.parseInt(toAdd);
    }
    System.out.println(sum);
  }
}

import java.util.Scanner;
import java.io.File;
import java.util.Arrays;

public class data {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numbers = new double[13];
        System.out.println("What is the name of the data file?");
        String fileName = scanner.nextLine();
        System.out.println("Reading data from file " + fileName);
        scanner.close();
        File file = new File(fileName);
        
        // Reading data into the array
        try {
            Scanner fileScanner = new Scanner(file);
            while (fileScanner.hasNextLine()) {
                for (int i = 0; i < 13; ++i) {
                    numbers[i] = Double.parseDouble(fileScanner.nextLine());
                }
            }
            fileScanner.close();
        } 
        catch(Exception e) {
            System.out.println("Invalid file name");
        }
        int length = numbers.length;

        // Outputting the data
        System.out.println("The data is: ");
        for (int i = 0; i < length; ++i) {
            System.out.print(numbers[i] + " ");
        }
        
        System.out.println("\nFinished reading file");
        System.out.println("The list is originially: " + Arrays.toString(numbers)); 
        
        // Finding the average 
        double sum = 0;
        for (int i = 0; i < length; ++i) {
            sum += numbers[i];
        }
        double average = sum / length;
        double sumOfDistances = 0;
        System.out.println("The average is: " + Math.round(average * 10000.00)/10000.00);
        
        // Finding the standard deviation
        for (int i = 0; i < length; ++i) {
            double diff = Math.pow((numbers[i] - average),2);
            sumOfDistances += diff;
        }
        double variance = sumOfDistances / (length - 1);
        double standardDev = Math.pow(variance, 0.5);
        System.out.println("The standard Deviation is: " + Math.round(standardDev * 10000.00)/10000.00);
        double upperBound = average + (2 * standardDev);
        double lowerBound = average - (2 * standardDev);
        System.out.println("Removing values outside the range " + Math.round(lowerBound * 10000.00)/10000.00 + " to " + Math.round(upperBound*10000.00)/10000.00);

        // Removing outliers
        double[] newList = new double[12];
        int removeIndex = 0;
        for (int i = 0; i < length; ++i) {
            if ((numbers[i] > upperBound) || (numbers[i] < lowerBound)) {
                System.out.println("Removed value: " + numbers[i]);
                removeIndex = i;
                break;
            }
        }
        for (int i = removeIndex; i < length - 1; ++i) {
            numbers[i] = numbers[i + 1];
        }
        for (int i = 0; i < length - 1; ++i) {
            newList[i] = numbers[i];
        }
        int newLength = newList.length;
        System.out.println("The list is now: "); 
        for (int i = 0; i < newLength; ++i) {
            System.out.print(newList[i] + " ");
        }

        // Finding the new average
        double newSum = 0;
        for (int i = 0; i < newLength; ++i) {
            newSum += newList[i];
        }
        double newAverage = newSum / newLength;
        double newSumOfDistances = 0;
        System.out.println("\nThe average with the extreme values removed is: " + Math.round(newAverage*10000.00)/10000.00);
        
        // Finding the new standard deviation
        for (int i = 0; i < 12; ++i) {
            double newDiff = Math.pow((newList[i] - newAverage),2);
            newSumOfDistances += newDiff;
        }
        double newVariance = newSumOfDistances / (newLength - 1);
        double newStandardDev = Math.pow(newVariance, 0.5);
        System.out.println("The standard Deviation with extreme values removed is: " + Math.round(newStandardDev*10000.00)/10000.00);
    }
}
import java.util.Scanner;

public class HRRN {
	public static void HRRN(int[] pid, int[] at, int[] bt) {

		// Number of processes
		int n = pid.length;

		// Create and initialize arrays for each of the desired statistics.
		int[] wait_time = new int[n];
		int[] turn_around_time = new int[n];
		int[] completion_time = new int[n];
		int[] remaining_bt = new int[n];

		int finished_processes = 0;
		int shortIndex = n;
		double avgwt = 0;
		double avgtat = 0;
		int timer = 0;

		// Duplicate bt onto remaining_bt to prevent mutation on the burst time
		for (int i = 0; i < n; i++) {
			remaining_bt[i] = bt[i];
		}

		// Completes when the amount of processes completed = the total amount of processes
		while (finished_processes != n) {
			double maxResponseRatio = 0;
			shortIndex = n;

			// Find the process with the highest response ratio
			for (int i = 0; i < n; i++) {
				
				if ((at[i] <= timer) && (remaining_bt[i] > 0)) {
				
					double responseRatio = (timer - at[i] + bt[i]) / (double)bt[i];
					
					if (responseRatio > maxResponseRatio) {
						maxResponseRatio = responseRatio;
						shortIndex = i;
					}
				}
			}

			if (shortIndex == n) {

				System.out.println("<System time " + timer + ">" + " system is idle");
				timer++;} 
			
			else {
				
				System.out.println("<System time " + timer + ">" + " process " + pid[shortIndex] + " starts runnning");
				completion_time[shortIndex] = timer + bt[shortIndex];

				for (int i = timer + 1; i <= completion_time[shortIndex] - 1; i++)
					
					System.out.println("<System time " + i + ">" + " process " + pid[shortIndex] + " is runnning");

				System.out.println("<System time " + completion_time[shortIndex] + ">" + " process " + pid[shortIndex] + " is finished.....");

				timer += bt[shortIndex];
				turn_around_time[shortIndex] = completion_time[shortIndex] - at[shortIndex];
				wait_time[shortIndex] = turn_around_time[shortIndex] - bt[shortIndex];
				remaining_bt[shortIndex] = 0;
				finished_processes++;

				System.out.print("Ready Queue: ");
				
				for (int i = 0; i < n; i++) {
			
					if ((at[i] <= timer) && (remaining_bt[i] > 0)) {
						System.out.print(" pid" + pid[i] + " ");
					}
				}
				
				System.out.println();
			}
		}

		System.out.println("PROCESS" + " " + "BURST TIME" + " " + "WAITING TIME" + " " + "TURNAROUND TIME");

		for (int i = 0; i < n; i++) {
			
			avgwt += wait_time[i];
			avgtat += turn_around_time[i];
			
			System.out.println(pid[i] + "\t" + bt[i] + "\t   " + wait_time[i] + "\t\t" + turn_around_time[i]);
		}

		avgwt = (double) avgwt / (double) n;
		avgtat = (double) avgtat / (double) n;

		System.out.println("Average waiting time = " + avgwt);
		System.out.println("Average turn around time = " + avgtat);
	}

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of processes: ");
		int n = sc.nextInt();

		int[] pid = new int[n];
		int[] at = new int[n];
		int[] bt = new int[n];

		for (int i = 0; i < n; i++) {

			pid[i] = i;
			sc.nextLine();

			System.out.println("Enter the arrival time for process " + i + ": ");
			at[i] = sc.nextInt();

			System.out.println("Enter the burst time for process " + i + ": ");
			bt[i] = sc.nextInt();
		}

		HRRN(pid, at, bt);
	}
}
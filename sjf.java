import java.util.Scanner;

public class sjf {
	
	public static void SJF( int[] pid, int[] at, int[] bt) {
		

		//number of processes
		int n = pid.length;
		
		//Initialize arrays
		int [] wait_time = new int[n];
		int [] turn_around_time = new int[n];
		int [] completion_time = new int[n];
		int [] remaining_bt = new int[n];

		
		int finished_processes = 0;
		
		int min = bt[0];
		
		int shortIndex = n;
		
		double  avgwt = 0, avgtat = 0;
        
		int counter = 0;
 
    	//sets the rem burst time to the process burst times before preceeding
        for (int i = 0; i < n ; i++) {
                      remaining_bt[i] = bt[i];
                      
        }

        
        while(finished_processes != n) {

			
			min = 1000000000;
			shortIndex = n;

			for(int i = 0; i < n; i++) {

				if((at[i] <= counter) && (remaining_bt[i] > 0) && (bt[i] < min))
				{
					min = bt[i];
					shortIndex = i;
				}
			}
			

			if(shortIndex== n) {
				System.out.println("<System time " + counter + ">" + " system is idle");
				counter++;
			}

			
			else {
				System.out.println("<System time " + counter + ">" + " process " + pid[shortIndex] + " starts runnning");
				completion_time[shortIndex] = counter + bt[shortIndex];
				
				for(int i = counter + 1; i <= completion_time[shortIndex] - 1; i++)
					 System.out.println("<System time " + i + ">" + " process " + pid[shortIndex] + " is runnning");
				
				System.out.println("<System time " + completion_time[shortIndex] + ">" + " process " + pid[shortIndex] + " is finished...");
				counter += bt[shortIndex];
				
				turn_around_time[shortIndex] = completion_time[shortIndex] - at[shortIndex];
				wait_time[shortIndex] = turn_around_time[shortIndex] - bt[shortIndex];
				remaining_bt[shortIndex] = 0;
				finished_processes++;
				
				System.out.print("Ready Queue: ");
				
				for(int i = 0; i < n; i++) {
				
					if((at[i] <= counter) && (remaining_bt[i] > 0)) {
					
						System.out.print(" pid" + pid[i] + " ");
					}
				}
				System.out.println();
			}
		}
		
		//calculate average wait time and average turn around time
		System.out.println("PROCESS " + "BURST TIME " + "WAITING TIME " + "TURN AROUND TIME ");
		
		for(int i = 0; i < n; i++) {
		
			avgwt += wait_time[i];
			avgtat += turn_around_time[i];
			
			System.out.println(pid[i] + "\t" + bt[i] + "\t   " + wait_time[i] + "\t\t" + turn_around_time[i]);
		}
		
		System.out.println("Average Wait Time: " + (double)(avgwt/n));
		System.out.println("Average Turn Around Time: " + (double)(avgtat/n));
	
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

		SJF(pid, at, bt);
	}
}
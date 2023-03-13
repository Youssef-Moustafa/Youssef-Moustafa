import java.util.Scanner;

public class  SRTF{
	
	
	static void ShortestRemainingTimeFirst(int[] pid, int[] at, int[] bt, int num_of_processes) {
		
		//number of processes
		int n = num_of_processes;
		
		int wait_time[] = new int[n];
		int turn_around_time[] = new int[n];
		
		float WTFinal = 0;
		float TTFinal = 0;
		
		int counter = 0;
		int completed = 0;
		int t = 0;
		int min = 100000;
		int shortest_time = 0;
		
		int complete_time;
		
		//keeps track of whether a process with the shortest remaining time has been found
		boolean found =  false;
		
		int remaining_bt[] = new int[n];
		
    	//sets the rem burst time to the process burst times before preceeding
		for (int i = 0; i < n; i++) {
			
			remaining_bt[i] = bt[i];
		}
		
		while (completed != n) {
			
			
			for (int j = 0; j < n; j++) {
				
				if ((at[j] <= t) && (remaining_bt[j] < min) && remaining_bt[j] > 0){
					
				min = remaining_bt[j];
				shortest_time = j;
				
				System.out.println("<System time " + counter + "> process " + pid[shortest_time] + " starts running");
				counter++;
				found = true;
					
				}
				
			}
			
			if (found == false) {
				
				t++;
				continue;
			}
			
			remaining_bt[shortest_time]--;
			System.out.println("<System time " + counter + "> process " + pid[shortest_time] + " is running");
			counter++;
			
			min = remaining_bt[shortest_time];
			
			
			if (min ==0)
				min = 1000000000;
			
			if (remaining_bt[shortest_time] == 0) {
				
				
				completed++;				
				found = false;
				
				
				System.out.println("System time " + counter + "> process " + pid[shortest_time] + " is finished");
				
				complete_time = t + 1;
				
				//calculate the wait time
				wait_time[shortest_time] = complete_time - bt[shortest_time] - at[shortest_time];
				
			
			
			if (wait_time[shortest_time] < 0)
				wait_time[shortest_time] = 0;
			
			}
			
			t++;
		}
		
	
		System.out.println("All processes are finished....");
		
		//turn around time calculation
		for (int i = 0; i < n; i++) {
			
			turn_around_time[i] = wait_time[i] + bt[i];
			
		}
		

		System.out.println("PROCESS " + "BURST TIME " + "WAITING TIME " + "TURN AROUND TIME");

		//calculates averages for the processors
		for (int i = 0; i < n; i++) {
			
			WTFinal = WTFinal + wait_time[i];
			TTFinal = TTFinal + turn_around_time[i];
			
			System.out.println("P" + i + "      " + bt[i] + "          " + wait_time[i] + "            " + turn_around_time[i]);
		}
		
		//calculate and print the averages
		float avgwt = WTFinal/(float)n;
		System.out.println("Average Wait Time: " + avgwt);
		float avgtat = TTFinal/(float)n;
		System.out.println("Average Turn Around Time: " + avgtat);
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
    

    ShortestRemainingTimeFirst(pid, at, bt, n);
    
    sc.close();
}
	}
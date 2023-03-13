import java.util.Scanner;

public class RR {

	public static void RoundR(int[] pid, int[] at, int[] bt, int quantum_time) {
		
		//number of processes
		int n = pid.length;
		
		//Initialize arrays
		int[] turn_around_time = new int[n];
		int[] wait_time = new int[n];
		int[] rem_burst_time = new int[n];
		
		float TTFinal = 0;
		float WTFinal = 0;
		int process_time = 0;
		int counter = 0;
	
		//sets the rem burst time to the process burst times before preceeding
		for (int i = 0; i < n; i++) {
			
			rem_burst_time[i] = bt[i];
		}
		
		while(true) {
			
			boolean processes_finished = true;
			
			for (int i = 0; i < n; i++){
				
				if (at[i]> process_time) {
					
					//iterate process time if the arrival time is greather than process time
					process_time++;
					processes_finished = false;
				}
				
				if ((at[i] <= process_time) && (rem_burst_time[i] > 0)) {
					processes_finished = false;
					
					//if quantum time is less than remaining burst time of current process i
					if (quantum_time < rem_burst_time[i]) {
						
						
						System.out.println("<System time " + counter + "> process " + i + " starts running");
						counter++;
						
						System.out.println("<System time " + counter + "> process " + i + " is running");
						counter++;
						

						process_time += quantum_time;
						
						rem_burst_time[i] -= quantum_time;
						
						System.out.println("<System time " + counter + "> process " + i + " is paused");
						
						counter++;
						
					}
					
					//if quantum time is greater than or equal to remaining burst time of current process i
					else {
						
						System.out.println("<System time " + counter + "> process " + i + " starts running");
						counter++;
						
						System.out.println("<System time " + counter + "> process " + i + " is running");
						counter++;
						
						process_time += rem_burst_time[i];
						
						wait_time[i] = process_time - bt[i];
						
						rem_burst_time[i] = 0;
						
						System.out.println("<System time " + counter + "> process" + i + " is finished");
						counter++;
						
						
					}
				}
				
				
				
			}
			
			if (processes_finished == true) {
				
				System.out.println("All processes finished.....");
				break;
				
			}
			
		}
			
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
        int qt;

        for (int i = 0; i < n; i++) {
        	
            pid[i] = i;
            sc.nextLine();
            
        	System.out.println("Enter the arrival time for process " + i + ": ");
            at[i] = sc.nextInt();
            
            
        	System.out.println("Enter the burst time for process " + i + ": ");
            bt[i] = sc.nextInt();
        }
        
        System.out.println("Enter a quantum time: ");
        qt = sc.nextInt();
        

        RoundR(pid, at, bt, qt);
        
        sc.close();
    }
}
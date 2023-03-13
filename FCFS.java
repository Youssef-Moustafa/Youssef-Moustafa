import java.util.Scanner;

public class FCFS {
	
	

	public static void FCFS(int[] processes, int[] at, int[] bt) {


		float TTFinal = 0;
		float WTFinal = 0;
		int counter = 0;

		//number of processes
		int n = processes.length;

		//array for turn around times
		int[] turn_around_time = new int[n];

		//array for waiting times
		int[] wait_time = new int[n];


		//First process, which has a wait time of 0
		wait_time[0] = 0;
		System.out.println("<System time " + counter + "> process 0 starts running");
		counter++;
		System.out.println("<System time " + counter + "> process 0 is running");
		counter++;
		System.out.println("<System time " + counter + "> process 0 is finished...");
		counter++;


		//second to nth process waiting time calculation
		for (int i = 1; i < n; i++) {

			System.out.println("<System time " + counter + ">" + " process " + i + " starts runnning");
			counter++;
			wait_time[i] = bt[i - 1] + wait_time[i - 1];
			System.out.println("<System time " + counter + ">" + " process " + i + " is runnning");
			counter++;		
			System.out.println("<System time " + counter + ">" + " process " + i + " is finished...");
			counter++;	

		}
		
		System.out.println("All process finished......");

	

	//turn around time calculation
	for (int i = 0; i < n; i++) {
		
		turn_around_time[i] = wait_time[i] + bt[i];
		
	}
	

	System.out.println("PROCESS " + "BURST TIME " + "WAITING TIME " + "TURN AROUND TIME");

	
	//calculate the average for the processors
	for (int i= 0; i < n; i++) {
		
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

        FCFS(pid, at, bt);
    }
}
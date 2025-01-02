import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class AutoCommit {


    
    // Path to your local repository
    private static final String REPO_PATH = "https://github.com/NishantRajora/python/tree/main/assignment";

    // Commit message template
    private static final String COMMIT_MESSAGE = "Auto-commit on ";

    public static void main(String[] args) {
        Timer timer = new Timer();
        long oneDay = 24 * 60 * 60 * 1000L; // 24 hours in milliseconds
        Date startTime = new Date(); // Start immediately

        // Schedule the task to run daily for 30 days
        timer.scheduleAtFixedRate(new CommitTask(), startTime, oneDay);

        // Schedule the timer to stop after 30 days
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println("Stopping the auto-commit scheduler after 30 days.");
                timer.cancel();
            }
        }, new Date(startTime.getTime() + (30 * oneDay)));
    }

    static class CommitTask extends TimerTask {
        @Override
        public void run() {
            try {
                // Format current date and time for the commit message
                String date = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());
                String commitMessage = COMMIT_MESSAGE + date;

                // Change to the repository directory
                File repoDir = new File(REPO_PATH);

                // Run Git commands
                runCommand(repoDir, "git", "add", ".");
                runCommand(repoDir, "git", "commit", "-m", commitMessage);
                runCommand(repoDir, "git", "push");

                System.out.println("Committed and pushed successfully at " + date);
            } catch (Exception e) {
                System.err.println("An error occurred: " + e.getMessage());
                e.printStackTrace();
            }
        }

        private void runCommand(File workingDir, String... command) throws IOException, InterruptedException {
            ProcessBuilder pb = new ProcessBuilder(command);
            pb.directory(workingDir);
            pb.redirectErrorStream(true);
            Process process = pb.start();
            process.waitFor();
        }
    }
}

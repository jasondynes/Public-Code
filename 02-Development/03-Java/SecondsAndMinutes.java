package coding.exercises;

public class SecondsAndMinutes {
    public static String getDurationString(int minutes, int seconds){
        if ((minutes >= 0) && (seconds >= 0 && seconds <=59)){
            int calcHours = minutes / 60;
            int calcMinutes = minutes % 60;
            return(calcHours + "h " + calcMinutes + "m " + seconds + "s");
        } else {
            return ("Invalid Value");
        }
    }
    public static String getDurationString(int seconds){
        if (seconds >= 0){
            int calcMinutes = seconds / 60;
            int remainingSeconds = seconds % 60;
            return getDurationString(calcMinutes, remainingSeconds);
        } else return ("Invalid Value");
    }

}

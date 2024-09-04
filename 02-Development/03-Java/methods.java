public class methods {
    public static void main(String[] args) {
        boolean gameOver = true;
        int score = 800;
        int levelCompleted = 5;
        int bonus = 100;
        int finalScore = calculateScore2(gameOver, score, levelCompleted, bonus);
        System.out.println("Your final score was " + finalScore);
//        calculateScore(true, 10000, 8, 200);
//        calculateScore2(true, 800, 5, 100);
//        calculateScore2(true, 10000, 8, 200);
//        calculateScore2(false, 10000, 8, 200);
        gameOver = true;
        score = 10000;
        levelCompleted = 8;
        bonus = 200;
        finalScore = calculateScore2(gameOver, score, levelCompleted, bonus);
        System.out.println("Your final score was " + finalScore);

        gameOver = false;
        score = 10000;
        levelCompleted = 8;
        bonus = 200;
        finalScore = calculateScore2(gameOver, score, levelCompleted, bonus);
        System.out.println("Your final score was " + finalScore);


        score = 1500;
        int position = calculateHighScorePosition(score);
        displayHighScorePosition("Jason", position);
        score = 900;
        position = calculateHighScorePosition(score);
        displayHighScorePosition("Jason", position);
        score = 400;
        position = calculateHighScorePosition(score);
        displayHighScorePosition("Jason", position);
        score = 50;
        position = calculateHighScorePosition(score);
        displayHighScorePosition("Jason", position);
    }
    public static void calculateScore(boolean gameOver, int score, int levelCompleted, int bonus) {
        if (gameOver == true) {
            int finalScore = score + (levelCompleted * bonus);
            finalScore += 2000;
            System.out.println("Your final score was " + finalScore);
        }
    }

    public static int calculateScore2(boolean gameOver, int score, int levelCompleted, int bonus) {
        if (gameOver == true) {
            int finalScore = score + (levelCompleted * bonus);
            finalScore += 2000;
            System.out.println("Your final score was " + finalScore);
            return finalScore;
        }
        return -1;
    }

    public static void displayHighScorePosition(String playerName, int highScorePosition){
        System.out.println("Player name: " + playerName + " managed to get into position " + highScorePosition);
    }

    public static int calculateHighScorePosition(int playerScore){
        // dodgy boundary value checks on 1000, 500 and 100 :-)
        if (playerScore >= 1000) {
            return 1;
        } else if (playerScore >=500){
            return 2;
        } else if (playerScore > 100) {
            return 3;
        }
        return 4;
    }
}

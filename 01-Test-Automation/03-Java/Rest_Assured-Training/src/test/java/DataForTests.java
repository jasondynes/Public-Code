import org.testng.annotations.*;

public class DataForTests {

    @DataProvider
    public Object[][] DataForPost(){
        // this example is static hard coded data
        Object[][] data = new Object[2][3];
        data[0][0] = "Albert";
        data[0][1] = "Einstein";
        data[0][2] = 2;
        data[1][0] = "Thomas";
        data[1][1] = "Edison";
        data[1][2] = 1;

        return data;
    }
    @DataProvider
    public Object[][] DataForPost2(){
        // more flexible implementation to above is below
        return new Object[][]{
                {"Graham", "Bell", 1},
                {"Henry", "Ford", 2}
        };
    }

    @DataProvider(name = "DeleteData")
    public Object[] DeleteData() {
        // more flexible implementation to above is below
        return new Object[]{
                4,5,6,7
        };
    }

}

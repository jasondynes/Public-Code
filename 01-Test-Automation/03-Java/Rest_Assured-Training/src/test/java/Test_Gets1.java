import io.restassured.response.*;
import org.testng.*;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class Test_Gets1 {
    //@org.junit.Test
    // full path can be used if alternating between TestNG and Junit as both are in dependencies
    @org.testng.annotations.Test
    void test_01(){
        Response response = get("http://swapi.dev/api/people/1/");
        System.out.println("getBody:\n" + response.getBody());
        System.out.println("getStatusCode:\n " + response.getStatusCode() + "\n");
        System.out.println("getStatusLine:\n" + response.getStatusLine() + "\n");
        System.out.println("getStatusLine:\n" + response.getTime() + "\n");
        System.out.println("asPrettyString:\n" + response.asPrettyString() + "\n");
        System.out.println("contentType:\n" + response.contentType() + "\n");
        //System.out.println("cookie:\n" + response.cookie());
        System.out.println("sessionId:\n" + response.sessionId() + "\n");
        System.out.println("getHeaders:\n" + response.getHeaders() + "\n");
        int statusCode = response.getStatusCode();
        System.out.println("Status code as a variable:\n" + statusCode + "\n");

    // Test Checks aka Assertions
        Assert.assertEquals(statusCode, 200);
        // documents are here: https://github.com/rest-assured/rest-assured/wiki/Usage
    }

    @org.testng.annotations.Test
    void test_02(){
                given()
                        .get("http://swapi.dev/api/people/1/")
                        .then().statusCode(200)
                        .body("name",equalTo("Luke Skywalker"))
                        .log().all();
    }
}

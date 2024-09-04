import io.restassured.http.*;
import org.json.simple.*;
import org.testng.annotations.*;
import static io.restassured.RestAssured.*;

public class Test_Puts {

    @Test
    void test_put1(){
        // code to do without a Map
        JSONObject request = new JSONObject();
        request.put("name", "Test Put1");
        request.put("job", "tester3");
        System.out.println("No MAP - Converted JSON Object:\n" + request);

        System.out.println("\n*************** PUT RESPONSE ****************\n");
        // POST command
        given()
                .header("Content-Type", "application/json")
                .contentType(ContentType.JSON)
                .body(request.toJSONString())
                .when()
                .put("https://reqres.in/api/users/2")
                .then()
                .statusCode(200)
                .log().all();
    }
}

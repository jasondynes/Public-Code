import io.restassured.http.*;
import org.json.simple.*;
import org.testng.annotations.*;

import static io.restassured.RestAssured.*;

public class Test_MockAPI_DataDriven2 extends DataForTests {


    @Test(dataProvider = "DataForPost2", priority = 2)
    public void test_post(String firstName, String lastName, int subjectId){
        JSONObject request = new JSONObject();
        request.put("firstName", firstName);
        request.put("lastName", lastName);
        request.put("subjectId", subjectId);

        baseURI = "http://localhost:3000/";
        given()
                .contentType(ContentType.JSON)
                .accept(ContentType.JSON)
                .header("Content-Type", "Application/json")
                .body(request.toJSONString())
                .when()
                .post("/users")
                .then()
                .statusCode(201)
                .log().all();
    }
}



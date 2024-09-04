import org.testng.annotations.*;

import static io.restassured.RestAssured.*;

public class Test_Delete {

    @Test
    void delete1(){
        given()
                .when()
                .delete("https://reqres.in/api/users/2")
                .then()
                .statusCode(204)
                .log().all();
    }
}

package utils;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.*;

public class ExcelUtils {
//        String excelPath = "./data/test+data.xlsx";
    static XSSFWorkbook workbook;
    static XSSFSheet sheet;

    public ExcelUtils(String excelPath, String sheetName) {
        try {
            // Use HSSFWorkbook for XLS format workbooks
            // Use XSSFWorkbook for XLSX format workbooks
            workbook = new XSSFWorkbook(excelPath);
        // reference by sheet name
            sheet = workbook.getSheet(sheetName);

        } catch (Exception exp) {
            System.out.println(exp.getMessage());
            System.out.println(exp.getCause());
            exp.printStackTrace();
        }
    }

    public static void getCellData(int rowNum, int colNum){
        DataFormatter formatter = new DataFormatter();
        Object dataValue = formatter.formatCellValue(sheet.getRow(rowNum).getCell(colNum));
        System.out.println(dataValue);
    }

    public static void getRowCount(){
            int rowCount = sheet.getPhysicalNumberOfRows();
            System.out.println("Number of rows: " + rowCount);
    }
}

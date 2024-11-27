from Demo import init_workbook, save_workbook, open_tgdd_page, get_data_tgdd, open_cellphone_page, get_data_cellphone

def main():
    # Khởi tạo Excel
    template_file = 'Report.xlsx'
    workbook, sheet = init_workbook(template_file)

    # Thegioididong
    tgdd_driver = open_tgdd_page()
    get_data_tgdd(tgdd_driver, sheet, start_row=3)
    tgdd_driver.quit()

    # CellphoneS
    cellphone_driver = open_cellphone_page()
    get_data_cellphone(cellphone_driver, sheet, start_row=3)
    cellphone_driver.quit()

    # Lưu file Excel
    save_workbook(workbook, template_file)

if __name__ == "__main__":
    main()

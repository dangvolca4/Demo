from Demo import init_csv, save_to_csv, open_tgdd_page, get_data_tgdd, open_cellphone_page, get_data_cellphone

def main():
    # Khởi tạo folder và file CSV
    report_folder = './Report'
    csv_file = init_csv(report_folder)

    # Thegioididong
    tgdd_driver = open_tgdd_page()
    tgdd_data = get_data_tgdd(tgdd_driver)
    save_to_csv(csv_file, tgdd_data)
    tgdd_driver.quit()

    # CellphoneS
    cellphone_driver = open_cellphone_page()
    cellphone_data = get_data_cellphone(cellphone_driver)
    save_to_csv(csv_file, cellphone_data)
    cellphone_driver.quit()

if __name__ == "__main__":
    main()

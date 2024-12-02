from Demo import init_csv, open_tgdd_page, get_data_tgdd, open_cellphone_page, get_data_cellphone

def main():
    # Khởi tạo file CSV
    csv_file = init_csv()  # Gọi hàm init_csv để tạo file CSV
    
    # Thegioididong
    tgdd_driver = open_tgdd_page()
    get_data_tgdd(tgdd_driver, csv_file)  # Truyền driver và csv_file vào hàm
    tgdd_driver.quit()

    # CellphoneS
    cellphone_driver = open_cellphone_page()
    get_data_cellphone(cellphone_driver, csv_file)  # Truyền driver và csv_file vào hàm
    cellphone_driver.quit()

if __name__ == "__main__":
    main()

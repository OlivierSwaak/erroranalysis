from erroranalysis.error_equations import error_multiplicate

# results in meters of measuring kitchen table
table_length = 2.304
table_length_err = 0.002
table_width = 0.798
table_width_err = 0.002

def table():
    area_table, area_table_err = error_multiplicate(table_length, table_length_err, table_width, table_width_err)
    print(f"Area of the kitchen table is: {area_table:.4f} \u00B1 {area_table_err:.4f} m")

if __name__ == "__main__":
    table()
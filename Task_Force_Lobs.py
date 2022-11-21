import pandas as pd
import  datetime
pd.options.mode.use_inf_as_na = True #empty strings characters '' or numpy.inf are not considered NA values (unless you set

def read_trans_data(file_path):
    read_df = pd.read_excel(file_path, sheet_name="APPR_MIGR", header=0, index_col=None)
    read_df['LOB_APPROVED'] = read_df['LOB_APPROVED'].str.strip().replace("'","")
    read_df.fillna('empty_value', inplace = True)

    return read_df

def check_misspell_is_ok(misspell_dict_df):
    if misspell_dict_df['CORRECT_VAL'].isna().sum() == 0:
        return False
    else:
        return True

def main():
# bringin initial data to consistancy, i.e for every approval instance approved lobs are gathered to list dict(N_APPR_INST: LOB_1, LOB_2, ...LOB_n)
    trans_data_df = read_trans_data(file_path)
    for index, row in trans_data_df.iterrows():  # adding index is vital, though it is not used !!!
        if row["N_APPR_INST"] not in temp_dict.keys():
            temp_dict[row["N_APPR_INST"]] = row["LOB_APPROVED"]
        else:
            if row["LOB_APPROVED"] not in temp_dict.get(row["N_APPR_INST"]):
                curr_dict_val = temp_dict.get(row["N_APPR_INST"])
                temp_dict[row["N_APPR_INST"]] = str(curr_dict_val) + ',' + str(row["LOB_APPROVED"])
    # this section can be uncommented for debugging
    # for k, i in temp_dict.items():
    #     print("{0}: {1}".format(k, i))
    # print("---------------------Printing SQL instructions & creating dictionary of misspellings: ---------------------")

    insert_instr = "insert into appr_inst_lob (N, N_APPR_INST, N_LOB, N_SOTR, DATE_CREATE) values (GEN_ID(n_appr_inst_lob, 1), {0}, {1}, 341, 'NOW');"
    # Checking if LOBs keyed by users are found either in DB_table.
    #                                           or in the misspelled values' dictionary
    # If found, creating SQL instruction. If Not, adding to misspelled values dictionary
    for cur_n_appr_inst in temp_dict.keys():
        for lob_name in str(temp_dict[cur_n_appr_inst]).split(','):
            try:
                lob_id = lob_df['N'].loc[lob_df['NAME'] == lob_name.strip()]
                print(insert_instr.format(cur_n_appr_inst, *lob_id))
            except:
                try:
                    lob_id = misspell_dict_df['CORRECT_N'].loc[misspell_dict_df['KEYED_VAL'] == lob_name.strip()]
                    print(insert_instr.format(cur_n_appr_inst, *lob_id))
                except:
                    misspell_dict_df.loc[len(misspell_dict_df.index)] = [lob_name.strip(), "",
                                                                         datetime.datetime.now().strftime(
                                                                             '%Y-%m-%d %H:%M:%S')]
                    empty_lines = 0
                    for index_mss, row_mss in misspell_dict_df.iterrows():
                        if row_mss['CORRECT_VAL'] == "":
                            empty_lines += 1
                    if len(misspell_dict_df) >= empty_lines:
                        with pd.ExcelWriter(meta_data_file, mode="a", engine="openpyxl",
                                            if_sheet_exists="replace") as writer:
                            misspell_dict_df.to_excel(writer, sheet_name='misspell_dict', index=False)
                        print("Update data in {0}".format(meta_data_file))

if __name__ == '__main__':
# path to folder with metadata and transactional
    working_folder = str(r"C:\......")  # path to be amended as needed
# config and setup of metadata
    meta_data_file = str(working_folder + r'\meta_data_file.xlsx')
    misspell_dict_df = pd.read_excel(meta_data_file, sheet_name="misspell_dict", header=0, index_col=None)
    lob_df = pd.read_excel(meta_data_file, sheet_name="LOBS", header=0, index_col=None)
    misspell_dict = dict()

# config and setup of transactional data
    file_path = str(working_folder + r'\Книга5.xlsx')
    temp_dict = dict()

# checkin that misspell table in meta_data file is filled entirely
    if check_misspell_is_ok(misspell_dict_df):
        print("Misspelling table should not contain empty cells. Update data in {0}".format(meta_data_file))
        exit()
    else:
        main()
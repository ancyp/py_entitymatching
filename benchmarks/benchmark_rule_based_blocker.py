# Write the benchmarking functions here.                                        
# See "Writing benchmarks" in the asv docs for more information.

import os
import sys

import magellan  as mg

p = mg.get_install_path()
datasets_path = os.sep.join([p, 'datasets', 'example_datasets'])

"""
class TimeBlockTablesElectronics:
    timeout = 20000.0

    def setup(self):
        path_for_A = os.sep.join([datasets_path, 'electronics', 'A.csv'])
        path_for_B = os.sep.join([datasets_path, 'electronics', 'B.csv'])
        self.A = mg.read_csv_metadata(path_for_A)
        mg.set_key(self.A, 'ID')
        self.B = mg.read_csv_metadata(path_for_B)
        mg.set_key(self.B, 'ID')
        self.feature_table = mg.get_features_for_blocking(self.A, self.B)

    def teardown(self):
        del self.A
        del self.B
        del self.feature_table
    
    def time_block_tables_name_cos(self):
        rb = mg.RuleBasedBlocker()
        rb.add_rule(['Name_Name_cos_dlm_dc0_dlm_dc0(ltuple,rtuple) < 0.3'],
                         self.feature_table)
        C = rb.block_tables(self.A, self.B, ['Name'], ['Name'])
        #C.to_csv('electronics', index=False)
        print >> sys.stderr, 'size of C:', len(C)
    
    def time_block_tables_features_jac(self):
        rb = mg.RuleBasedBlocker()
        rb.add_rule(['Features_Features_jac_qgm_3_qgm_3(ltuple,rtuple) < 0.6'],
                         self.feature_table)
        C = rb.block_tables(self.A, self.B, ['Features'], ['Features'])
        print >> sys.stderr, 'size of C:', len(C)
    
class TimeBlockTablesAnime:
    timeout = 10000.0

    def setup(self):
        path_for_A = os.sep.join([datasets_path, 'anime', 'A.csv'])
        path_for_B = os.sep.join([datasets_path, 'anime', 'B.csv'])
        self.A = mg.read_csv_metadata(path_for_A)
        mg.set_key(self.A, 'ID')
        self.B = mg.read_csv_metadata(path_for_B)
        mg.set_key(self.B, 'ID')
        self.feature_table = mg.get_features_for_blocking(self.A, self.B)

    def teardown(self):
        del self.A
        del self.B
        del self.feature_table

    def time_block_tables(self):
        rb = mg.RuleBasedBlocker()
        rb.add_rule(['Title_Title_jac_qgm_3_qgm_3(ltuple,rtuple) < 0.4'],
                         self.feature_table)
        C = rb.block_tables(self.A, self.B, ['Title'], ['Title'])
        print >> sys.stderr, 'size of C:', len(C)

class TimeBlockTablesBooks:
    timeout = 10000.0

    def setup(self):
        path_for_A = os.sep.join([datasets_path, 'books', 'A.csv'])
        path_for_B = os.sep.join([datasets_path, 'books', 'B.csv'])
        self.A = mg.read_csv_metadata(path_for_A)
        mg.set_key(self.A, 'ID')
        self.B = mg.read_csv_metadata(path_for_B)
        mg.set_key(self.B, 'ID')
        self.feature_table = mg.get_features_for_blocking(self.A, self.B)
        self.rb = mg.RuleBasedBlocker()

    def teardown(self):
        del self.A
        del self.B
        del self.feature_table
        del self.rb

    def time_block_tables(self):
        self.rb.add_rule(['ISBN13_ISBN13_exm(ltuple, rtuple) < 0.4'],
                         self.feature_table)
        C = self.rb.block_tables(self.A, self.B,
                                 ['Title','Author','ISBN13','Publisher','Publication_Date'],
                                 ['Title','Author','ISBN13','Publisher','Publication_Date'])
        print >> sys.stderr, 'size of C:', len(C)

class TimeBlockTablesMovies:
    timeout = 10000.0

    def setup(self):
        path_for_A = os.sep.join([datasets_path, 'movies', 'A.csv'])
        path_for_B = os.sep.join([datasets_path, 'movies', 'B.csv'])
        self.A = mg.read_csv_metadata(path_for_A)
        mg.set_key(self.A, 'id')
        self.B = mg.read_csv_metadata(path_for_B)
        mg.set_key(self.B, 'id')
        self.feature_table = mg.get_features_for_blocking(self.A, self.B)

    def teardown(self):
        del self.A
        del self.B
        del self.feature_table

    def time_block_tables(self):
        rb = mg.RuleBasedBlocker()
        rb.add_rule(['movie_name_movie_name_jac_qgm_3_qgm_3(ltuple,rtuple) < 0.6'],
                         self.feature_table)
        C = rb.block_tables(self.A, self.B,
                                 ['movie_name','year','directors','actors','critic_rating','genre','pg_rating','duration'],
                                 ['movie_name','year','directors','actors','movie_rating','genre','duration'])
        print >> sys.stderr, 'size of C:', len(C)

"""
class TimeBlockCandsetRestaurants:
    timeout = 600.0

    def setup(self):
        path_for_A = os.sep.join([datasets_path, 'restaurants', 'A.csv'])
        path_for_B = os.sep.join([datasets_path, 'restaurants', 'B.csv'])
        A = mg.read_csv_metadata(path_for_A)
        mg.set_key(A, 'ID')
        B = mg.read_csv_metadata(path_for_B)
        mg.set_key(B, 'ID')
        ob = mg.OverlapBlocker()
        self.C = ob.block_tables(A, B, 'ADDRESS', 'ADDRESS', overlap_size=4,
			         l_output_attrs=['NAME', 'PHONENUMBER', 'ADDRESS'],
                                 r_output_attrs=['NAME', 'PHONENUMBER', 'ADDRESS'])
        feature_table = mg.get_features_for_blocking(A,B)
        self.rb = mg.RuleBasedBlocker()
        self.rb.add_rule(['ADDRESS_ADDRESS_jac_qgm_3_qgm_3(ltuple,rtuple) < 0.44'],
                         feature_table)

    def teardown(self):
        del self.C
        del self.rb

    def time_block_candset(self):
        D = self.rb.block_candset(self.C)
        print >> sys.stderr, 'size of C:', len(self.C)
        print >> sys.stderr, 'size of D:', len(D)

"""
class TimeBlockCandsetEbooks:
    timeout = 600.0

    def setup(self):
        path_for_A = os.sep.join([datasets_path, 'ebooks', 'A.csv'])
        path_for_B = os.sep.join([datasets_path, 'ebooks', 'B.csv'])
        A = mg.read_csv_metadata(path_for_A)
        mg.set_key(A, 'record_id')
        B = mg.read_csv_metadata(path_for_B)
        mg.set_key(B, 'record_id')
        ob = mg.OverlapBlocker()
        self.C = ob.block_tables(A, B, 'title', 'title', overlap_size=2,
                                 rem_stop_words = True,
                                 l_output_attrs=['title', 'author', 'publisher', 'date'],
                                 r_output_attrs=['title', 'author', 'publisher', 'date'])
        feature_table = mg.get_features_for_blocking(A,B)
        self.rb = mg.RuleBasedBlocker()
        self.rb.add_rule(['date_date_lev(ltuple, rtuple) < 0.6'], feature_table)

    def teardown(self):
        del self.C
        del self.rb

    def time_block_candset(self):
        D = self.rb.block_candset(self.C)
        print >> sys.stderr, 'size of C:', len(self.C)
        print >> sys.stderr, 'size of D:', len(D)
"""

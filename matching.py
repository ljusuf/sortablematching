import ast
import re


#listing_list = [[{},'Not Matched'], [{}, 'Matched']]
listing_list = []
for listing_entry in open('listings.txt').readlines():
    listing_list += [[ast.literal_eval(listing_entry), 'Not Matched']]

#product_list =[{},{}]
product_list = []
for product_entry in open('products.txt').readlines():
    product_list += [ast.literal_eval(product_entry)]



#match_result = {'product_name':[{},{},{}], 
#               'product_name': [{},{},{}]}

match_result = {}


for product_info in product_list:
    #comparison logic here
    for list_info in listing_list:
        if (list_info[1] == 'Not Matched') and \
        (list_info[0]['manufacturer'].strip().lower() == product_info['manufacturer'].strip().lower()) and \
        re.search(product_info['model'].strip().lower(), list_info[0]['title'].strip().lower()):
            if match_result.has_key(product_info['product_name']):
                match_result[product_info['product_name']] += [list_info[0]]
            else:
                match_result.update({product_info['product_name']:[list_info[0]]})
            #change the status of listing item to 'Matched'
            list_info[1] = 'Matched'

result_file = open('results.txt','w')
for key in match_result:
    result_file.write('{"product_name":'+ key + ', "listings":' + str(match_result[key]) + '} \n')
result_file.close()





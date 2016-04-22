#Program to fetch google search results from custom search api

__author__ = 'shreyavaidy'

import pprint
import json
from googleapiclient.discovery import build

def main():

  print('Search Results: \n')

  service = build('customsearch', 'v1',
            developerKey="AIzaSyBS4Ul8eDzE-WKOnxxm9bW4zVPZ00gngVs")

  request = service.cse().list(
      q='extension',
      lr='lang_en',
      exactTerms='extension',
      excludeTerms='Games Apps Themes',
      filter='1',
      cx='004717870502135588221:db5tddqamui',
  )
  response=request.execute()

#prints the response of the custom search
  pprint.pprint(response)


#printing the output in json format

  # Create an output file name in the format "searchresp.json"
  output_dir = './output/'
  output_fname = output_dir + 'searchresponse' + '.json'
  #creating file object output_f
  output_f = open(output_fname, 'ab')

  #writing to an object
  output1 = json.dumps(response, sort_keys=True, indent=4)

  #writing into file object
  output_f.write(output1)

#writing extension URLs from json object to text file
  op_fname = output_dir + 'URLs'+'.txt'
  op_f = open(op_fname,'w')

  parsed_json=json.loads(output1)

  for item in parsed_json['items']:
    urls=(item['link'])
    output2 = json.dumps(urls, sort_keys=True)
    #writing URLs into the file object
    op_f.write(output2)
    op_f.write('\n')

  #closing file objects
  output_f.close()
  op_f.close()

  print('\n\nOutput written.')

#calling the main function
if __name__ == '__main__':
  main()



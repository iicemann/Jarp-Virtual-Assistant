import wolframalpha
input = input("Question: ")
app_id = 'AX5Y26-KXAGRT3QP5'
client = wolframalpha.Client(app_id)
res = client.query(input)
if res['@success'] == 'false':
	print('Not resloved')
else:
	pod0 = res['pod'][0]['subpod']['plaintext']
	print(pod0)
	# pod[1] may contains the answer
	pod1 = res['pod'][1]
	# checking if pod1 has primary=true or title=result|definition
	if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
	  # extracting result from pod1
		result = pod1['subpod']['plaintext']
		print(result)
		print

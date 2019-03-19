import basc_py4chan
from db_helper import DbHelper

board_name = 'pol'

board = basc_py4chan.Board(board_name)

thread_ids = board.get_all_thread_ids()

dbHelper = DbHelper()

for thread_id in thread_ids:

	thread = board.get_thread(thread_id)

	# print thread information
	if thread.sticky:
		continue
	# information from the OP
	topic = thread.topic
	print('Thread Name:', topic.subject)

	row_id = dbHelper.insert_thread(topic.subject, board_name, thread_id)

	if row_id != 0:
		for post in thread.posts:
			print(post.subject)
			dbHelper.insert_post(post.subject, post.text_comment, row_id)
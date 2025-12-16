import os


def data_operator(mode, data=False):
	with open('data.txt', mode) as file:
		if mode == 'r':
			return file.read()
		elif mode == 'a':
			file.write('\n' + data)
		elif mode == 'w':
			file.write(data)


welcome = '''
-------------------------------------------------------
    ###      #   #      ###   ####  #  ##   #   ###    
   #   #    # # # #    #   #    #   #  # #  #  #       
   #####   #   #   #   #####   #    #  #  # #  #  ##   
   #   #  #         #  #   #  ####  #  #   ##   ###    
   -------------------------------------------------   
             #####   ###   ###    ###                  
               #    #   #  #  #  #   #                 
               #    #   #  #  #  #   #                 
               #     ###   ###    ###                  
                                                       
                  © 2025 AMAZING TODO                  
-------------------------------------------------------


'''


def main():
		ce = 'Press Enter to continue!'
		print(welcome)
		input(ce)
		print('\n' * 40)
		while True:
			try:
				print('\n' * 40)
				print('----------------')
				print('1) Show Tasks')
				print('2) Add Task')
				print('3) Complete Task')
				print('4) Delete Task')
				print('5) Exit')
				print('----------------')
				choice = int(input('Enter a number: '))
				if choice == 1:
					print('\n' * 40)
					if len(data_operator('r')) < 1:
						print('You don\'t have any tasks!')
					print(data_operator('r'))
					input(ce)
				elif choice == 2:
					print('\n' * 40)
					task_num = str(len(data_operator('r').split('\n')))
					temp = input('Enter your task:\n')
					if len(temp.strip()) == 0:
						print('You should enter something!')
					else:
						task = task_num + ') ' + temp
						data_operator('a', task)
						print('\nTask added!')
					input(ce)
				elif choice == 3:
					print('\n' * 40)
					completed_task = int(input('Enter task\'s number to mark it as a completed:\n'))
					data = data_operator('r').split('\n')
					if '(Completed)' not in data[completed_task]:
						data[completed_task] = data[completed_task] + '(Completed)'
						data_operator('w', '\n'.join(data))
						print('Task marked as a completed!')
					else:
						print('This task has already completed!')
					input(ce)
				elif choice == 4:
					print('\n' * 40)
					deleted_task = int(input('Enter task\'s number to delete it:\n'))
					data = data_operator('r').split('\n')
					data.pop(deleted_task)
					for index, value in enumerate(data):
						if index != 0:
							data[index] = str(index) + value[1:]
					data_operator('w', '\n'.join(data))
					print('Task deleted!')
					input(ce)
				elif choice == 5:
					print('\n' * 40)
					print('Bye!')
					input()
					break
				else:
					print('\n' * 40)
					print('You should enter numbers from 1 to 5!')
					input(ce)
			except ValueError:
				print('\n' * 40)
				print('You should enter a number!')
				input(ce)
			except IndexError:
				print('\n' * 40)
				print('There is no such task!')
				input(ce)


if __name__ == '__main__':
	if os.path.isfile('data.txt') == False:
		with open('data.txt', 'w') as file:
			file.write('')
	main()




# TODO: CLI
"""
PROJECT: To-Do List Manager
============================
Level: Beginner
Author: Onur Çakılı
Description: A simple command-line to-do list application
"""

import json
from datetime import datetime

class TodoList:
    """To-Do List Manager"""
    
    def __init__(self):
        """Initialize to-do list"""
        self.tasks = []
        self.task_id_counter = 1
    
    def add_task(self, description, priority="Medium"):
        """Add a new task"""
        task = {
            'id': self.task_id_counter,
            'description': description,
            'priority': priority,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.task_id_counter += 1
        return task['id']
    
    def view_tasks(self, filter_by=None):
        """View all tasks or filtered tasks"""
        if not self.tasks:
            print("\nNo tasks found!")
            return
        
        # Filter tasks
        if filter_by == 'completed':
            filtered_tasks = [t for t in self.tasks if t['completed']]
            title = "COMPLETED TASKS"
        elif filter_by == 'pending':
            filtered_tasks = [t for t in self.tasks if not t['completed']]
            title = "PENDING TASKS"
        else:
            filtered_tasks = self.tasks
            title = "ALL TASKS"
        
        if not filtered_tasks:
            print(f"\nNo {filter_by or 'tasks'} found!")
            return
        
        print(f"\n{'=' * 80}")
        print(f"{title:^80}")
        print('=' * 80)
        print(f"{'ID':<5} {'Description':<40} {'Priority':<10} {'Status':<10} {'Created':<15}")
        print('-' * 80)
        
        for task in filtered_tasks:
            status = "✓ Done" if task['completed'] else "○ Pending"
            priority_symbol = {
                'High': '🔴',
                'Medium': '🟡',
                'Low': '🟢'
            }.get(task['priority'], '')
            
            print(f"{task['id']:<5} {task['description']:<40} "
                  f"{priority_symbol} {task['priority']:<8} {status:<10} "
                  f"{task['created_at']:<15}")
        
        print('=' * 80)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    print(f"\nTask {task_id} is already completed!")
                else:
                    task['completed'] = True
                    task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"\nTask {task_id} marked as completed!")
                return True
        print(f"\nTask {task_id} not found!")
        return False
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                print(f"\nTask {task_id} deleted: {deleted_task['description']}")
                return True
        print(f"\nTask {task_id} not found!")
        return False
    
    def update_task(self, task_id, new_description=None, new_priority=None):
        """Update task description or priority"""
        for task in self.tasks:
            if task['id'] == task_id:
                if new_description:
                    task['description'] = new_description
                if new_priority:
                    task['priority'] = new_priority
                task['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\nTask {task_id} updated successfully!")
                return True
        print(f"\nTask {task_id} not found!")
        return False
    
    def get_statistics(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t['completed'])
        pending = total - completed
        
        if total > 0:
            completion_rate = (completed / total) * 100
        else:
            completion_rate = 0
        
        # Priority breakdown
        priority_count = {
            'High': sum(1 for t in self.tasks if t['priority'] == 'High'),
            'Medium': sum(1 for t in self.tasks if t['priority'] == 'Medium'),
            'Low': sum(1 for t in self.tasks if t['priority'] == 'Low')
        }
        
        print(f"\n{'=' * 40}")
        print("TASK STATISTICS")
        print('=' * 40)
        print(f"Total Tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        print(f"Completion Rate: {completion_rate:.1f}%")
        print(f"\nPriority Breakdown:")
        print(f"  🔴 High: {priority_count['High']}")
        print(f"  🟡 Medium: {priority_count['Medium']}")
        print(f"  🟢 Low: {priority_count['Low']}")
        print('=' * 40)
    
    def save_to_file(self, filename='tasks.json'):
        """Save tasks to file"""
        try:
            with open(filename, 'w') as f:
                json.dump({'tasks': self.tasks, 'counter': self.task_id_counter}, f, indent=2)
            print(f"\nTasks saved to {filename}")
        except Exception as e:
            print(f"\nError saving tasks: {e}")
    
    def load_from_file(self, filename='tasks.json'):
        """Load tasks from file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = data['tasks']
                self.task_id_counter = data['counter']
            print(f"\nTasks loaded from {filename}")
        except FileNotFoundError:
            print(f"\nNo saved tasks found.")
        except Exception as e:
            print(f"\nError loading tasks: {e}")

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 40)
    print("TO-DO LIST MANAGER")
    print("=" * 40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. Complete Task")
    print("6. Update Task")
    print("7. Delete Task")
    print("8. Statistics")
    print("9. Save Tasks")
    print("10. Load Tasks")
    print("11. Exit")
    print("=" * 40)

def main():
    """Main application function"""
    todo = TodoList()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-11): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            print("\nPriority levels: High, Medium, Low")
            priority = input("Enter priority (default: Medium): ").strip() or "Medium"
            task_id = todo.add_task(description, priority)
            print(f"\nTask added successfully! (ID: {task_id})")
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            todo.view_tasks('pending')
        
        elif choice == '4':
            todo.view_tasks('completed')
        
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Invalid task ID!")
        
        elif choice == '6':
            try:
                task_id = int(input("Enter task ID to update: "))
                new_desc = input("Enter new description (leave blank to skip): ").strip()
                new_priority = input("Enter new priority (leave blank to skip): ").strip()
                todo.update_task(task_id, new_desc or None, new_priority or None)
            except ValueError:
                print("Invalid task ID!")
        
        elif choice == '7':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid task ID!")
        
        elif choice == '8':
            todo.get_statistics()
        
        elif choice == '9':
            todo.save_to_file()
        
        elif choice == '10':
            todo.load_from_file()
        
        elif choice == '11':
            print("\nThank you for using To-Do List Manager!")
            break
        
        else:
            print("\nInvalid choice! Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Demo mode
    print("=" * 40)
    print("TO-DO LIST DEMO")
    print("=" * 40)
    
    todo = TodoList()
    
    # Add sample tasks
    todo.add_task("Complete Python project", "High")
    todo.add_task("Study for exam", "High")
    todo.add_task("Buy groceries", "Medium")
    todo.add_task("Call dentist", "Low")
    todo.add_task("Read book", "Low")
    
    # View all tasks
    todo.view_tasks()
    
    # Complete some tasks
    todo.complete_task(1)
    todo.complete_task(3)
    
    # View pending tasks
    todo.view_tasks('pending')
    
    # Get statistics
    todo.get_statistics()
    
    print("\n" + "=" * 40)
    print("DEMO COMPLETED!")
    print("=" * 40)
    
    # Uncomment to run interactive mode
    # main()

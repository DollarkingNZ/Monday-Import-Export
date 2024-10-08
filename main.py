import requests
# from monday import MondayClient
# monday = MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMzMTUyNTU2OSwiYWFpIjoxMSwidWlkIjoxMjEyMzM4MCwiaWFkIjoiMjAyNC0wMy0xMlQwMToyMzoxOC4zNDRaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NTM5OTQ4NCwicmduIjoidXNlMSJ9.xlo0ona083Z93wFsPViYHGCpWt6Fzf4aHRM2D7-EyxM')
# monday.items.create_item(board_id='6239120871', group_id='today', item_name='do a thing')

api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMzMTUyNTU2OSwiYWFpIjoxMSwidWlkIjoxMjEyMzM4MCwiaWFkIjoiMjAyNC0wMy0xMlQwMToyMzoxOC4zNDRaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NTM5OTQ4NCwicmduIjoidXNlMSJ9.xlo0ona083Z93wFsPViYHGCpWt6Fzf4aHRM2D7-EyxM'

# Set the URL for the Monday.com API
url = 'https://api.monday.com/v2'

# Set headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

q1 = '''
{
  me {
    name
  }
  boards(limit: 1) {
    name
    columns {
      title
      id
      type
    }
    groups {
      title
      id
    }
  }
}
'''

q2 = '''
query GetBoardItems { boards(ids: 6239120871) {  
    items_page(limit: 5) {  
      items {  
        id  
        name  
        column_values {  
          id  
          value  
        }  
      }  
    }  
  }  
}
'''

q3 = '''
# Example: Update column value
# The query will update the status column on a specifc board item
# from whatever it currently is to "Done"

mutation UpdateColumnValue{
  change_simple_column_value (board_id: 6239120871, item_id: 6239120885, column_id: "status", value: "Complete") {
    id
  }
}
'''

q4 = '''
# Example: Create a new item
# Here's an example of how you might create an item with
# the name "Great Example", set the owner to a user with 
# the ID 12345, and set the status to "New":
  
mutation CreateNewItem{
  create_item (board_id: 6239120871, item_name: "New Item") {
    id
  }
}
'''


# Make the request
response = requests.post(url, headers=headers, json={'query': q4})

# Print the response
print(response.json())

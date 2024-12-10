import { useState } from 'react';
import { useQuery } from 'react-query';
import { 
  List, 
  ListItem, 
  ListItemText, 
  Paper, 
  TextField, 
  MenuItem 
} from '@mui/material';
import { apiClient } from '../../api/apiClient';

function ChatList() {
  const [selectedRobotId, setSelectedRobotId] = useState(0);
  
  const { data: chatLogs, isLoading } = useQuery(
    ['chatLogs', selectedRobotId],
    () => apiClient.getChatLogs(selectedRobotId)
  );

  if (isLoading) return 'Loading...';

  return (
    <>
      <TextField
        select
        label="Select Robot"
        value={selectedRobotId}
        onChange={(e) => setSelectedRobotId(e.target.value)}
        fullWidth
        sx={{ mb: 2 }}
      >
        <MenuItem value={0}>Robot 0</MenuItem>
        <MenuItem value={1}>Robot 1</MenuItem>
      </TextField>
      
      <List>
        {chatLogs?.data.map((log) => (
          <Paper key={log.log_id} sx={{ mb: 1 }}>
            <ListItem>
              <ListItemText
                primary={log.content}
                secondary={`Time: ${new Date(log.registered).toLocaleString()}`}
              />
            </ListItem>
          </Paper>
        ))}
      </List>
    </>
  );
}

export default ChatList;
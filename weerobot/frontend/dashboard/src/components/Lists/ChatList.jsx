import React, { useState } from 'react';
import { useQuery } from 'react-query';
import { 
  List, 
  ListItem, 
  ListItemText, 
  Paper, 
  CircularProgress,
  TextField,
  MenuItem
} from '@mui/material';
import { apiClient } from '../../api/apiClient';

function ChatList() {
  const [selectedRobotId, setSelectedRobotId] = useState(0);

  const { data, isLoading, isError } = useQuery(
    ['chatLogs', selectedRobotId],
    async () => {
      const response = await apiClient.getChatLogs(selectedRobotId);
      return response.data;
    }
  );

  if (isLoading) {
    return <CircularProgress />;
  }

  if (isError) {
    return <div>Error loading chat logs</div>;
  }

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
        <MenuItem value={1}>Robot 1</MenuItem>
      </TextField>

      <List>
        {data?.map((log) => (
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
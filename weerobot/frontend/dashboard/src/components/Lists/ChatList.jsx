import React from 'react';
import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper, CircularProgress, Box } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function ChatList() {
  const { data, isLoading, isError } = useQuery('chatLogs', async () => {
    const response = await apiClient.getChatLogs();
    return response.data;
  });

  if (isLoading) {
    return <CircularProgress size={20} />;
  }

  if (isError) {
    return <Box sx={{ color: 'error.main' }}>Error loading chat logs</Box>;
  }

  // 최대 5개만 표시
  const displayData = data?.slice(0, 5) || [];

  return (
    <List disablePadding>
      {displayData.map((chat) => (
        <Paper key={chat.log_id} sx={{ mb: 0.5 }}>
          <ListItem dense>
            <ListItemText
              primary={`Log ID: ${chat.log_id}`}
              secondary={`Robot ID: ${chat.robot_id} | Message: ${chat.content}`}
              primaryTypographyProps={{ fontSize: '0.9rem' }}
              secondaryTypographyProps={{ fontSize: '0.8rem' }}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default ChatList;
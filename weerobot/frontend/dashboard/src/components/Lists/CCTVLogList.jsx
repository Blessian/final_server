import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function CCTVLogList() {
  const { data: logs, isLoading } = useQuery('cctvLogs', apiClient.getCCTVLogs);

  if (isLoading) return 'Loading...';

  return (
    <List>
      {logs?.data.map((log) => (
        <Paper key={log.log_id} sx={{ mb: 1 }}>
          <ListItem>
            <ListItemText
              primary={`Log ID: ${log.log_id}`}
              secondary={`CCTV ID: ${log.cctv_id} | Time: ${new Date(log.registered).toLocaleString()}`}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default CCTVLogList;
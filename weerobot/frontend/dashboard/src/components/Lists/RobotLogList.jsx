import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function RobotLogList() {
  const { data: logs, isLoading } = useQuery('robotLogs', apiClient.getRobotLogs);

  if (isLoading) return 'Loading...';

  return (
    <List>
      {logs?.data.map((log) => (
        <Paper key={log.log_id} sx={{ mb: 1 }}>
          <ListItem>
            <ListItemText
              primary={`Log ID: ${log.log_id}`}
              secondary={`Robot ID: ${log.robot_id} | Status: ${log.status} | Time: ${new Date(log.registered).toLocaleString()}`}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default RobotLogList;
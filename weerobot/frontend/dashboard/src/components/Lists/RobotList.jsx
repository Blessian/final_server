import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper, Chip } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function RobotList() {
  const { data: robots, isLoading } = useQuery('robots', apiClient.getRobots);

  if (isLoading) return 'Loading...';

  return (
    <List>
      {robots?.data.map((robot) => (
        <Paper key={robot.robot_id} sx={{ mb: 1 }}>
          <ListItem>
            <ListItemText
              primary={`Robot ID: ${robot.robot_id}`}
              secondary={
                <Chip
                  label={`Status: ${robot.status}`}
                  color={robot.status === 0 ? 'success' : 'error'}
                  size="small"
                />
              }
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default RobotList;
import { Box, Paper, Tabs, Tab } from '@mui/material';
import { useState } from 'react';
import RobotList from './Lists/RobotList';
import CCTVList from './Lists/CCTVList';
import CCTVLogList from './Lists/CCTVLogList';
import RobotLogList from './Lists/RobotLogList';
import ChatList from './Lists/ChatList';

function DataSection() {
  const [tabValue, setTabValue] = useState(0);

  return (
    <Box sx={{ flex: 1, p: 2 }}>
      <Paper elevation={3} sx={{ height: '100%', p: 2 }}>
        <Tabs
          value={tabValue}
          onChange={(e, newValue) => setTabValue(newValue)}
        >
          <Tab label="Robots" />
          <Tab label="CCTVs" />
          <Tab label="CCTV Logs" />
          <Tab label="Robot Logs" />
          <Tab label="Chat" />
        </Tabs>
        <Box sx={{ mt: 2, height: 'calc(100% - 48px)', overflow: 'auto' }}>
          {tabValue === 0 && <RobotList />}
          {tabValue === 1 && <CCTVList />}
          {tabValue === 2 && <CCTVLogList />}
          {tabValue === 3 && <RobotLogList />}
          {tabValue === 4 && <ChatList />}
        </Box>
      </Paper>
    </Box>
  );
}

export default DataSection;
import { Modal, Box, IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import { useStore } from '../hooks/useStore';

function VideoModal() {
  const { videoModalOpen, setVideoModalOpen, currentVideo } = useStore();

  return (
    <Modal
      open={videoModalOpen}
      onClose={() => setVideoModalOpen(false)}
      aria-labelledby="video-modal"
    >
      <Box
        sx={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: '80%',
          maxWidth: 800,
          bgcolor: 'background.paper',
          boxShadow: 24,
          p: 4,
          borderRadius: 2,
        }}
      >
        <IconButton
          sx={{ position: 'absolute', right: 8, top: 8 }}
          onClick={() => setVideoModalOpen(false)}
        >
          <CloseIcon />
        </IconButton>
        <Box sx={{ width: '100%', aspectRatio: '16/9', bgcolor: 'black' }}>
          {currentVideo && (
            <img
              src={`data:image/jpeg;base64,${currentVideo}`}
              alt="CCTV Stream"
              style={{ width: '100%', height: '100%', objectFit: 'contain' }}
            />
          )}
        </Box>
      </Box>
    </Modal>
  );
}

export default VideoModal;
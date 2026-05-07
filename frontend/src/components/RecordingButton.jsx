function RecordingButton({
  loading,
  isRecording,
  startRecording,
  stopRecording,
}) {

  return (
    <button
      className="record-button"
      disabled={loading}
      onClick={
        isRecording
          ? stopRecording
          : startRecording
      }
    >
      {loading
        ? "Processing..."
        : isRecording
        ? "Stop Recording"
        : "Start Recording"}
    </button>
  );
}

export default RecordingButton;
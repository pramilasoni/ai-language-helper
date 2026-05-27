function ModeSelector({
  mode,
  setMode,
  sourceLanguage,
  setSourceLanguage,
  targetLanguage,
  setTargetLanguage,
  practiceLanguage,
  setPracticeLanguage,
}) {
  return (
    <div className="mode-selector">
      <label>Choose Mode</label>

      <select
        value={mode}
        onChange={(e) => setMode(e.target.value)}
      >
        <option value="translation">Translation</option>
        <option value="perfection">Perfection</option>
      </select>

      {mode === "translation" && (
        <>
          <label>Source Language</label>
          <input
            value={sourceLanguage}
            onChange={(e) => setSourceLanguage(e.target.value)}
            placeholder="Example: Danish"
          />

          <label>Target Language</label>
          <input
            value={targetLanguage}
            onChange={(e) => setTargetLanguage(e.target.value)}
            placeholder="Example: English"
          />
        </>
      )}

      {mode === "perfection" && (
        <>
          <label>Practice Language</label>
          <input
            value={practiceLanguage}
            onChange={(e) => setPracticeLanguage(e.target.value)}
            placeholder="Example: Danish"
          />
        </>
      )}
    </div>
  );
}

export default ModeSelector;
depends = ('ITKPyBase', 'ITKCommon', )
templates = (
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISS2', True, 'itk::Image< signed short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISS3', True, 'itk::Image< signed short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISS4', True, 'itk::Image< signed short,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUC4', True, 'itk::Image< unsigned char,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBUC4', True, 'itk::Image< itk::RGBPixel< unsigned char >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBAUC4', True, 'itk::Image< itk::RGBAPixel< unsigned char >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUS4', True, 'itk::Image< unsigned short,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIF2', True, 'itk::Image< float,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIF3', True, 'itk::Image< float,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIF4', True, 'itk::Image< float,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF24', True, 'itk::Image< itk::Vector< float,2 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF24', True, 'itk::Image< itk::CovariantVector< float,2 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF34', True, 'itk::Image< itk::Vector< float,3 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF34', True, 'itk::Image< itk::CovariantVector< float,3 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF44', True, 'itk::Image< itk::Vector< float,4 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF44', True, 'itk::Image< itk::CovariantVector< float,4 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferID2', True, 'itk::Image< double,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISSRTD22', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD22', True, 'itk::Image< itk::Vector< double,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD22', True, 'itk::Image< itk::CovariantVector< double,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD32', True, 'itk::Image< itk::Vector< double,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD32', True, 'itk::Image< itk::CovariantVector< double,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD42', True, 'itk::Image< itk::Vector< double,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD42', True, 'itk::Image< itk::CovariantVector< double,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferID3', True, 'itk::Image< double,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISSRTD33', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD23', True, 'itk::Image< itk::Vector< double,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD23', True, 'itk::Image< itk::CovariantVector< double,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD33', True, 'itk::Image< itk::Vector< double,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD33', True, 'itk::Image< itk::CovariantVector< double,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD43', True, 'itk::Image< itk::Vector< double,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD43', True, 'itk::Image< itk::CovariantVector< double,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferID4', True, 'itk::Image< double,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISSRTD44', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 4 >, 4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD24', True, 'itk::Image< itk::Vector< double,2 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD24', True, 'itk::Image< itk::CovariantVector< double,2 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD34', True, 'itk::Image< itk::Vector< double,3 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD34', True, 'itk::Image< itk::CovariantVector< double,3 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD44', True, 'itk::Image< itk::Vector< double,4 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD44', True, 'itk::Image< itk::CovariantVector< double,4 >,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUI2', True, 'itk::Image< unsigned int,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUI3', True, 'itk::Image< unsigned int,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUI4', True, 'itk::Image< unsigned int,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUL2', True, 'itk::Image< unsigned long,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUL3', True, 'itk::Image< unsigned long,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUL4', True, 'itk::Image< unsigned long,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISI2', True, 'itk::Image< signed int,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISI3', True, 'itk::Image< signed int,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISI4', True, 'itk::Image< signed int,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVISS2', True, 'itk::VectorImage< signed short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUC2', True, 'itk::VectorImage< unsigned char,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUS2', True, 'itk::VectorImage< unsigned short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIF2', True, 'itk::VectorImage< float,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVID2', True, 'itk::VectorImage< double,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVISS3', True, 'itk::VectorImage< signed short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUC3', True, 'itk::VectorImage< unsigned char,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUS3', True, 'itk::VectorImage< unsigned short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIF3', True, 'itk::VectorImage< float,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVID3', True, 'itk::VectorImage< double,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVISS4', True, 'itk::VectorImage< signed short,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUC4', True, 'itk::VectorImage< unsigned char,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUS4', True, 'itk::VectorImage< unsigned short,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIF4', True, 'itk::VectorImage< float,4 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVID4', True, 'itk::VectorImage< double,4 >'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSS', True, 'signed short'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUC', True, 'unsigned char'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUS', True, 'unsigned short'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlF', True, 'float'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlD', True, 'double'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUI', True, 'unsigned int'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUL', True, 'unsigned long'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSC', True, 'signed char'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSI', True, 'signed int'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSL', True, 'signed long'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLSS', True, 'unsigned long long,signed short'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLF', True, 'unsigned long long,float'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLD', True, 'unsigned long long,double'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCSS', True, 'unsigned char,signed short'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCF', True, 'unsigned char,float'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCD', True, 'unsigned char,double'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLVF2', True, 'unsigned long long,itk::Vector< float,2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLPF2', True, 'unsigned long long,itk::Point< float,2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLMF22', True, 'unsigned long long, itk::Matrix< float, 2, 2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLVD2', True, 'unsigned long long,itk::Vector< double,2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLPD2', True, 'unsigned long long,itk::Point< double,2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLMD22', True, 'unsigned long long, itk::Matrix< double, 2, 2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLVF3', True, 'unsigned long long,itk::Vector< float,3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLPF3', True, 'unsigned long long,itk::Point< float,3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLMF33', True, 'unsigned long long, itk::Matrix< float, 3, 3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLVD3', True, 'unsigned long long,itk::Vector< double,3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLPD3', True, 'unsigned long long,itk::Point< double,3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLMD33', True, 'unsigned long long, itk::Matrix< double, 3, 3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLVF4', True, 'unsigned long long,itk::Vector< float,4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLPF4', True, 'unsigned long long,itk::Point< float,4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLMF44', True, 'unsigned long long, itk::Matrix< float, 4, 4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLVD4', True, 'unsigned long long,itk::Vector< double,4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLPD4', True, 'unsigned long long,itk::Point< double,4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLMD44', True, 'unsigned long long, itk::Matrix< double, 4, 4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCO2', True, 'unsigned char,itk::Offset< 2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUICID2', True, 'unsigned int,itk::ContinuousIndex< double,2 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCO3', True, 'unsigned char,itk::Offset< 3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUICID3', True, 'unsigned int,itk::ContinuousIndex< double,3 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCO4', True, 'unsigned char,itk::Offset< 4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUICID4', True, 'unsigned int,itk::ContinuousIndex< double,4 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUIVUC1', True, 'unsigned int,itk::Vector< unsigned char,1 >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLSULL', True, 'unsigned long long, std::set< unsigned long long >'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLULL', True, 'unsigned long long, unsigned long long'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLUI', True, 'unsigned long long, unsigned int'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLUC', True, 'unsigned long long, unsigned char'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerULLUS', True, 'unsigned long long, unsigned short'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUIULL', True, 'unsigned int, unsigned long long'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUIUI', True, 'unsigned int, unsigned int'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUIUC', True, 'unsigned int, unsigned char'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUIUS', True, 'unsigned int, unsigned short'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCULL', True, 'unsigned char, unsigned long long'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCUI', True, 'unsigned char, unsigned int'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCUC', True, 'unsigned char, unsigned char'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUCUS', True, 'unsigned char, unsigned short'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUSULL', True, 'unsigned short, unsigned long long'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUSUI', True, 'unsigned short, unsigned int'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUSUC', True, 'unsigned short, unsigned char'),
  ('PyVectorContainer', 'itk::PyVectorContainer', 'itkPyVectorContainerUSUS', True, 'unsigned short, unsigned short'),
)

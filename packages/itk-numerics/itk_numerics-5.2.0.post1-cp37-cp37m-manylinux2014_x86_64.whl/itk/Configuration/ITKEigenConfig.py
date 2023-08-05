depends = ('ITKPyBase', 'ITKImageFilterBase', )
templates = (
  ('EigenAnalysis2DImageFilter', 'itk::EigenAnalysis2DImageFilter', 'itkEigenAnalysis2DImageFilterIF2IF2IVF22', True, 'itk::Image< float,2 >, itk::Image< float,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('EigenAnalysis2DImageFilter', 'itk::EigenAnalysis2DImageFilter', 'itkEigenAnalysis2DImageFilterID2ID2IVF22', True, 'itk::Image< double,2 >, itk::Image< double,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
)

depends = ('ITKPyBase', 'ITKTransform', 'ITKMesh', 'ITKImageFunction', 'ITKCommon', )
templates = (
  ('SpatialObjectProperty', 'itk::SpatialObjectProperty', 'itkSpatialObjectProperty', True),
  ('MetaEvent', 'itk::MetaEvent', 'itkMetaEvent', True),
  ('SpatialObject', 'itk::SpatialObject', 'itkSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkSpatialObject2_Pointer', False, 'itk::SpatialObject< 2  >'),
  ('SpatialObject', 'itk::SpatialObject', 'itkSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkSpatialObject3_Pointer', False, 'itk::SpatialObject< 3  >'),
  ('SpatialObject', 'itk::SpatialObject', 'itkSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkSpatialObject4_Pointer', False, 'itk::SpatialObject< 4  >'),
  ('SpatialObjectPoint', 'itk::SpatialObjectPoint', 'itkSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkSpatialObjectPoint2', False, 'itk::SpatialObjectPoint< 2  >'),
  ('SpatialObjectPoint', 'itk::SpatialObjectPoint', 'itkSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkSpatialObjectPoint3', False, 'itk::SpatialObjectPoint< 3  >'),
  ('SpatialObjectPoint', 'itk::SpatialObjectPoint', 'itkSpatialObjectPoint4', True, '4'),
  ('vector', 'std::vector', 'vectoritkSpatialObjectPoint4', False, 'itk::SpatialObjectPoint< 4  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkPointBasedSpatialObject2_Pointer', False, 'itk::PointBasedSpatialObject< 2  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkPointBasedSpatialObject3_Pointer', False, 'itk::PointBasedSpatialObject< 3  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkPointBasedSpatialObject4_Pointer', False, 'itk::PointBasedSpatialObject< 4  >'),
  ('ContourSpatialObjectPoint', 'itk::ContourSpatialObjectPoint', 'itkContourSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkContourSpatialObjectPoint2', False, 'itk::ContourSpatialObjectPoint< 2  >'),
  ('ContourSpatialObjectPoint', 'itk::ContourSpatialObjectPoint', 'itkContourSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkContourSpatialObjectPoint3', False, 'itk::ContourSpatialObjectPoint< 3  >'),
  ('ContourSpatialObjectPoint', 'itk::ContourSpatialObjectPoint', 'itkContourSpatialObjectPoint4', True, '4'),
  ('vector', 'std::vector', 'vectoritkContourSpatialObjectPoint4', False, 'itk::ContourSpatialObjectPoint< 4  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectContour2', True, '2, itk::ContourSpatialObjectPoint<2>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectContour2_Pointer', False, 'itk::PointBasedSpatialObject< 2, itk::ContourSpatialObjectPoint<2>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectContour3', True, '3, itk::ContourSpatialObjectPoint<3>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectContour3_Pointer', False, 'itk::PointBasedSpatialObject< 3, itk::ContourSpatialObjectPoint<3>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectContour4', True, '4, itk::ContourSpatialObjectPoint<4>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectContour4_Pointer', False, 'itk::PointBasedSpatialObject< 4, itk::ContourSpatialObjectPoint<4>  >'),
  ('ContourSpatialObjectEnums', 'itk::ContourSpatialObjectEnums', 'itkContourSpatialObjectEnums', False),
  ('ContourSpatialObject', 'itk::ContourSpatialObject', 'itkContourSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkContourSpatialObject2_Pointer', False, 'itk::ContourSpatialObject< 2  >'),
  ('ContourSpatialObject', 'itk::ContourSpatialObject', 'itkContourSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkContourSpatialObject3_Pointer', False, 'itk::ContourSpatialObject< 3  >'),
  ('ContourSpatialObject', 'itk::ContourSpatialObject', 'itkContourSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkContourSpatialObject4_Pointer', False, 'itk::ContourSpatialObject< 4  >'),
  ('TubeSpatialObjectPoint', 'itk::TubeSpatialObjectPoint', 'itkTubeSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkTubeSpatialObjectPoint2', False, 'itk::TubeSpatialObjectPoint< 2  >'),
  ('TubeSpatialObjectPoint', 'itk::TubeSpatialObjectPoint', 'itkTubeSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkTubeSpatialObjectPoint3', False, 'itk::TubeSpatialObjectPoint< 3  >'),
  ('TubeSpatialObjectPoint', 'itk::TubeSpatialObjectPoint', 'itkTubeSpatialObjectPoint4', True, '4'),
  ('vector', 'std::vector', 'vectoritkTubeSpatialObjectPoint4', False, 'itk::TubeSpatialObjectPoint< 4  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectTube2', True, '2, itk::TubeSpatialObjectPoint<2>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectTube2_Pointer', False, 'itk::PointBasedSpatialObject< 2, itk::TubeSpatialObjectPoint<2>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectTube3', True, '3, itk::TubeSpatialObjectPoint<3>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectTube3_Pointer', False, 'itk::PointBasedSpatialObject< 3, itk::TubeSpatialObjectPoint<3>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectTube4', True, '4, itk::TubeSpatialObjectPoint<4>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectTube4_Pointer', False, 'itk::PointBasedSpatialObject< 4, itk::TubeSpatialObjectPoint<4>  >'),
  ('TubeSpatialObject', 'itk::TubeSpatialObject', 'itkTubeSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkTubeSpatialObject2_Pointer', False, 'itk::TubeSpatialObject< 2  >'),
  ('TubeSpatialObject', 'itk::TubeSpatialObject', 'itkTubeSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkTubeSpatialObject3_Pointer', False, 'itk::TubeSpatialObject< 3  >'),
  ('TubeSpatialObject', 'itk::TubeSpatialObject', 'itkTubeSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkTubeSpatialObject4_Pointer', False, 'itk::TubeSpatialObject< 4  >'),
  ('DTITubeSpatialObjectPointEnums', 'itk::DTITubeSpatialObjectPointEnums', 'itkDTITubeSpatialObjectPointEnums', False),
  ('DTITubeSpatialObjectPoint', 'itk::DTITubeSpatialObjectPoint', 'itkDTITubeSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkDTITubeSpatialObjectPoint3', False, 'itk::DTITubeSpatialObjectPoint< 3  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectDTITube3', True, '3, itk::DTITubeSpatialObjectPoint<3>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectDTITube3_Pointer', False, 'itk::PointBasedSpatialObject< 3, itk::DTITubeSpatialObjectPoint<3>  >'),
  ('DTITubeSpatialObject', 'itk::DTITubeSpatialObject', 'itkDTITubeSpatialObject3', True, '3'),
  ('LineSpatialObjectPoint', 'itk::LineSpatialObjectPoint', 'itkLineSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkLineSpatialObjectPoint2', False, 'itk::LineSpatialObjectPoint< 2  >'),
  ('LineSpatialObjectPoint', 'itk::LineSpatialObjectPoint', 'itkLineSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkLineSpatialObjectPoint3', False, 'itk::LineSpatialObjectPoint< 3  >'),
  ('LineSpatialObjectPoint', 'itk::LineSpatialObjectPoint', 'itkLineSpatialObjectPoint4', True, '4'),
  ('vector', 'std::vector', 'vectoritkLineSpatialObjectPoint4', False, 'itk::LineSpatialObjectPoint< 4  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectLine2', True, '2, itk::LineSpatialObjectPoint<2>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectLine2_Pointer', False, 'itk::PointBasedSpatialObject< 2, itk::LineSpatialObjectPoint<2>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectLine3', True, '3, itk::LineSpatialObjectPoint<3>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectLine3_Pointer', False, 'itk::PointBasedSpatialObject< 3, itk::LineSpatialObjectPoint<3>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectLine4', True, '4, itk::LineSpatialObjectPoint<4>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectLine4_Pointer', False, 'itk::PointBasedSpatialObject< 4, itk::LineSpatialObjectPoint<4>  >'),
  ('LineSpatialObject', 'itk::LineSpatialObject', 'itkLineSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkLineSpatialObject2_Pointer', False, 'itk::LineSpatialObject< 2  >'),
  ('LineSpatialObject', 'itk::LineSpatialObject', 'itkLineSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkLineSpatialObject3_Pointer', False, 'itk::LineSpatialObject< 3  >'),
  ('LineSpatialObject', 'itk::LineSpatialObject', 'itkLineSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkLineSpatialObject4_Pointer', False, 'itk::LineSpatialObject< 4  >'),
  ('SurfaceSpatialObjectPoint', 'itk::SurfaceSpatialObjectPoint', 'itkSurfaceSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkSurfaceSpatialObjectPoint2', False, 'itk::SurfaceSpatialObjectPoint< 2  >'),
  ('SurfaceSpatialObjectPoint', 'itk::SurfaceSpatialObjectPoint', 'itkSurfaceSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkSurfaceSpatialObjectPoint3', False, 'itk::SurfaceSpatialObjectPoint< 3  >'),
  ('SurfaceSpatialObjectPoint', 'itk::SurfaceSpatialObjectPoint', 'itkSurfaceSpatialObjectPoint4', True, '4'),
  ('vector', 'std::vector', 'vectoritkSurfaceSpatialObjectPoint4', False, 'itk::SurfaceSpatialObjectPoint< 4  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectSurface2', True, '2, itk::SurfaceSpatialObjectPoint<2>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectSurface2_Pointer', False, 'itk::PointBasedSpatialObject< 2, itk::SurfaceSpatialObjectPoint<2>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectSurface3', True, '3, itk::SurfaceSpatialObjectPoint<3>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectSurface3_Pointer', False, 'itk::PointBasedSpatialObject< 3, itk::SurfaceSpatialObjectPoint<3>  >'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObjectSurface4', True, '4, itk::SurfaceSpatialObjectPoint<4>'),
  ('list', 'std::list', 'listitkPointBasedSpatialObjectSurface4_Pointer', False, 'itk::PointBasedSpatialObject< 4, itk::SurfaceSpatialObjectPoint<4>  >'),
  ('SurfaceSpatialObject', 'itk::SurfaceSpatialObject', 'itkSurfaceSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkSurfaceSpatialObject2_Pointer', False, 'itk::SurfaceSpatialObject< 2  >'),
  ('SurfaceSpatialObject', 'itk::SurfaceSpatialObject', 'itkSurfaceSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkSurfaceSpatialObject3_Pointer', False, 'itk::SurfaceSpatialObject< 3  >'),
  ('SurfaceSpatialObject', 'itk::SurfaceSpatialObject', 'itkSurfaceSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkSurfaceSpatialObject4_Pointer', False, 'itk::SurfaceSpatialObject< 4  >'),
  ('LandmarkSpatialObject', 'itk::LandmarkSpatialObject', 'itkLandmarkSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkLandmarkSpatialObject2_Pointer', False, 'itk::LandmarkSpatialObject< 2  >'),
  ('LandmarkSpatialObject', 'itk::LandmarkSpatialObject', 'itkLandmarkSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkLandmarkSpatialObject3_Pointer', False, 'itk::LandmarkSpatialObject< 3  >'),
  ('LandmarkSpatialObject', 'itk::LandmarkSpatialObject', 'itkLandmarkSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkLandmarkSpatialObject4_Pointer', False, 'itk::LandmarkSpatialObject< 4  >'),
  ('BlobSpatialObject', 'itk::BlobSpatialObject', 'itkBlobSpatialObject2', True, '2'),
  ('BlobSpatialObject', 'itk::BlobSpatialObject', 'itkBlobSpatialObject3', True, '3'),
  ('BlobSpatialObject', 'itk::BlobSpatialObject', 'itkBlobSpatialObject4', True, '4'),
  ('PolygonSpatialObject', 'itk::PolygonSpatialObject', 'itkPolygonSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkPolygonSpatialObject2_Pointer', False, 'itk::PolygonSpatialObject< 2  >'),
  ('PolygonSpatialObject', 'itk::PolygonSpatialObject', 'itkPolygonSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkPolygonSpatialObject3_Pointer', False, 'itk::PolygonSpatialObject< 3  >'),
  ('PolygonSpatialObject', 'itk::PolygonSpatialObject', 'itkPolygonSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkPolygonSpatialObject4_Pointer', False, 'itk::PolygonSpatialObject< 4  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2UC', True, '2,unsigned char'),
  ('list', 'std::list', 'listitkImageSpatialObject2UC_Pointer', False, 'itk::ImageSpatialObject< 2,unsigned char  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2SS', True, '2,signed short'),
  ('list', 'std::list', 'listitkImageSpatialObject2SS_Pointer', False, 'itk::ImageSpatialObject< 2,signed short  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2US', True, '2,unsigned short'),
  ('list', 'std::list', 'listitkImageSpatialObject2US_Pointer', False, 'itk::ImageSpatialObject< 2,unsigned short  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2F', True, '2,float'),
  ('list', 'std::list', 'listitkImageSpatialObject2F_Pointer', False, 'itk::ImageSpatialObject< 2,float  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2D', True, '2,double'),
  ('list', 'std::list', 'listitkImageSpatialObject2D_Pointer', False, 'itk::ImageSpatialObject< 2,double  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3UC', True, '3,unsigned char'),
  ('list', 'std::list', 'listitkImageSpatialObject3UC_Pointer', False, 'itk::ImageSpatialObject< 3,unsigned char  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3SS', True, '3,signed short'),
  ('list', 'std::list', 'listitkImageSpatialObject3SS_Pointer', False, 'itk::ImageSpatialObject< 3,signed short  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3US', True, '3,unsigned short'),
  ('list', 'std::list', 'listitkImageSpatialObject3US_Pointer', False, 'itk::ImageSpatialObject< 3,unsigned short  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3F', True, '3,float'),
  ('list', 'std::list', 'listitkImageSpatialObject3F_Pointer', False, 'itk::ImageSpatialObject< 3,float  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3D', True, '3,double'),
  ('list', 'std::list', 'listitkImageSpatialObject3D_Pointer', False, 'itk::ImageSpatialObject< 3,double  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject4UC', True, '4,unsigned char'),
  ('list', 'std::list', 'listitkImageSpatialObject4UC_Pointer', False, 'itk::ImageSpatialObject< 4,unsigned char  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject4SS', True, '4,signed short'),
  ('list', 'std::list', 'listitkImageSpatialObject4SS_Pointer', False, 'itk::ImageSpatialObject< 4,signed short  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject4US', True, '4,unsigned short'),
  ('list', 'std::list', 'listitkImageSpatialObject4US_Pointer', False, 'itk::ImageSpatialObject< 4,unsigned short  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject4F', True, '4,float'),
  ('list', 'std::list', 'listitkImageSpatialObject4F_Pointer', False, 'itk::ImageSpatialObject< 4,float  >'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject4D', True, '4,double'),
  ('list', 'std::list', 'listitkImageSpatialObject4D_Pointer', False, 'itk::ImageSpatialObject< 4,double  >'),
  ('ImageMaskSpatialObject', 'itk::ImageMaskSpatialObject', 'itkImageMaskSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkImageMaskSpatialObject2_Pointer', False, 'itk::ImageMaskSpatialObject< 2  >'),
  ('ImageMaskSpatialObject', 'itk::ImageMaskSpatialObject', 'itkImageMaskSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkImageMaskSpatialObject3_Pointer', False, 'itk::ImageMaskSpatialObject< 3  >'),
  ('ImageMaskSpatialObject', 'itk::ImageMaskSpatialObject', 'itkImageMaskSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkImageMaskSpatialObject4_Pointer', False, 'itk::ImageMaskSpatialObject< 4  >'),
  ('ArrowSpatialObject', 'itk::ArrowSpatialObject', 'itkArrowSpatialObject2', True, '2'),
  ('ArrowSpatialObject', 'itk::ArrowSpatialObject', 'itkArrowSpatialObject3', True, '3'),
  ('ArrowSpatialObject', 'itk::ArrowSpatialObject', 'itkArrowSpatialObject4', True, '4'),
  ('BoxSpatialObject', 'itk::BoxSpatialObject', 'itkBoxSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkBoxSpatialObject2_Pointer', False, 'itk::BoxSpatialObject< 2  >'),
  ('BoxSpatialObject', 'itk::BoxSpatialObject', 'itkBoxSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkBoxSpatialObject3_Pointer', False, 'itk::BoxSpatialObject< 3  >'),
  ('BoxSpatialObject', 'itk::BoxSpatialObject', 'itkBoxSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkBoxSpatialObject4_Pointer', False, 'itk::BoxSpatialObject< 4  >'),
  ('EllipseSpatialObject', 'itk::EllipseSpatialObject', 'itkEllipseSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkEllipseSpatialObject2_Pointer', False, 'itk::EllipseSpatialObject< 2  >'),
  ('EllipseSpatialObject', 'itk::EllipseSpatialObject', 'itkEllipseSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkEllipseSpatialObject3_Pointer', False, 'itk::EllipseSpatialObject< 3  >'),
  ('EllipseSpatialObject', 'itk::EllipseSpatialObject', 'itkEllipseSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkEllipseSpatialObject4_Pointer', False, 'itk::EllipseSpatialObject< 4  >'),
  ('GaussianSpatialObject', 'itk::GaussianSpatialObject', 'itkGaussianSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkGaussianSpatialObject2_Pointer', False, 'itk::GaussianSpatialObject< 2  >'),
  ('GaussianSpatialObject', 'itk::GaussianSpatialObject', 'itkGaussianSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkGaussianSpatialObject3_Pointer', False, 'itk::GaussianSpatialObject< 3  >'),
  ('GaussianSpatialObject', 'itk::GaussianSpatialObject', 'itkGaussianSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkGaussianSpatialObject4_Pointer', False, 'itk::GaussianSpatialObject< 4  >'),
  ('GroupSpatialObject', 'itk::GroupSpatialObject', 'itkGroupSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkGroupSpatialObject2_Pointer', False, 'itk::GroupSpatialObject< 2  >'),
  ('GroupSpatialObject', 'itk::GroupSpatialObject', 'itkGroupSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkGroupSpatialObject3_Pointer', False, 'itk::GroupSpatialObject< 3  >'),
  ('GroupSpatialObject', 'itk::GroupSpatialObject', 'itkGroupSpatialObject4', True, '4'),
  ('list', 'std::list', 'listitkGroupSpatialObject4_Pointer', False, 'itk::GroupSpatialObject< 4  >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2ISS2', True, 'itk::SpatialObject< 2 >,itk::Image< signed short,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2IUC2', True, 'itk::SpatialObject< 2 >,itk::Image< unsigned char,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2IUS2', True, 'itk::SpatialObject< 2 >,itk::Image< unsigned short,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2IF2', True, 'itk::SpatialObject< 2 >,itk::Image< float,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2ID2', True, 'itk::SpatialObject< 2 >,itk::Image< double,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3ISS3', True, 'itk::SpatialObject< 3 >,itk::Image< signed short,3 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3IUC3', True, 'itk::SpatialObject< 3 >,itk::Image< unsigned char,3 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3IUS3', True, 'itk::SpatialObject< 3 >,itk::Image< unsigned short,3 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3IF3', True, 'itk::SpatialObject< 3 >,itk::Image< float,3 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3ID3', True, 'itk::SpatialObject< 3 >,itk::Image< double,3 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO4ISS4', True, 'itk::SpatialObject< 4 >,itk::Image< signed short,4 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO4IUC4', True, 'itk::SpatialObject< 4 >,itk::Image< unsigned char,4 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO4IUS4', True, 'itk::SpatialObject< 4 >,itk::Image< unsigned short,4 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO4IF4', True, 'itk::SpatialObject< 4 >,itk::Image< float,4 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO4ID4', True, 'itk::SpatialObject< 4 >,itk::Image< double,4 >'),
  ('CastSpatialObjectFilter', 'itk::CastSpatialObjectFilter', 'itkCastSpatialObjectFilter2', True, '2'),
  ('CastSpatialObjectFilter', 'itk::CastSpatialObjectFilter', 'itkCastSpatialObjectFilter3', True, '3'),
  ('CastSpatialObjectFilter', 'itk::CastSpatialObjectFilter', 'itkCastSpatialObjectFilter4', True, '4'),
  ('MetaConverterBase', 'itk::MetaConverterBase', 'itkMetaConverterBase2', True, '2'),
  ('MetaConverterBase', 'itk::MetaConverterBase', 'itkMetaConverterBase3', True, '3'),
  ('MetaConverterBase', 'itk::MetaConverterBase', 'itkMetaConverterBase4', True, '4'),
)
